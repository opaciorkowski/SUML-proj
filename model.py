#pip install -r requirements.txt
import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import keras
import numpy as np 
import tensorflow as tf
import pandas as pd

# Data 
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data Visualization
import plotly.express as px
import matplotlib.pyplot as plt

# Model 
from keras.models import Sequential, load_model
from keras.layers import GlobalAvgPool2D as GAP, Dense, Dropout

# Callbacks 
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Pre-Trained Model
from tensorflow.keras.applications import ResNet50, ResNet50V2, InceptionV3, Xception, ResNet152, ResNet152V2

# Class Names
root_path = 'Vegetable Images/train/'
class_names = sorted(os.listdir(root_path))
n_classes = len(class_names)

# Class Distribution
class_dis = [len(os.listdir(root_path + name)) for name in class_names]

# Show
print(f"Total Number of Classes : {n_classes} \nClass Names : {class_names}")

# Visualize 
fig = px.pie(names=class_names, values=class_dis, title="Class Distribution", hole=0.4)
fig.update_layout({'title':{'x':0.5}})
fig.show()

# Initialize Generator
train_gen = ImageDataGenerator(rescale=1/255., rotation_range=10)
valid_gen = ImageDataGenerator(rescale=1/255.)
test_gen = ImageDataGenerator(rescale=1/255.)

# Load Data
train_ds = train_gen.flow_from_directory(root_path, class_mode='binary', target_size=(256,256), shuffle=True, batch_size=32)
valid_ds = valid_gen.flow_from_directory(root_path.replace('train','validation'), class_mode='binary', target_size=(256,256), shuffle=True, batch_size=32)
test_ds = test_gen.flow_from_directory(root_path.replace('train', 'test'), class_mode='binary', target_size=(256,256), shuffle=True, batch_size=32)

def show_images(GRID=[5,5], model=None, size=(20,20), data=train_ds):
    n_rows = GRID[0]
    n_cols = GRID[1]
    n_images = n_cols * n_rows
    
    i = 1
    plt.figure(figsize=size)
    for images, labels in data:
        id = np.random.randint(32)
        image, label = images[id], class_names[int(labels[id])]
        
        plt.subplot(n_rows, n_cols, i)
        plt.imshow(image)
        
        if model is None:
            title = f"Class : {label}"
        else:
            pred = class_names[int(np.argmax(model.predict(image[np.newaxis, ...])))]
            title = f"Org : {label}, Pred : {pred}"
        
        plt.title(title)
        plt.axis('off')
        
        i+=1
        if i>=(n_images+1):
            break
            
    plt.tight_layout()
    plt.show()

show_images()

# Pre-Trained Model 
base_model = ResNet50V2(input_shape=(256,256,3), include_top=False)
base_model.trainable = False

# Model Architecture
name = "ResNet50V2"
model = Sequential([
    base_model,
    GAP(),
    Dense(256, activation='relu', kernel_initializer='he_normal'),
    Dense(n_classes, activation='softmax')
], name=name)

# Callbacks
checkpoint_path = "ResNet50V2.weights.h5"  # Use .weights.h5 for weights only
cbs = [
    EarlyStopping(patience=3, restore_best_weights=True),
    ModelCheckpoint(checkpoint_path, save_weights_only=True, save_best_only=True)
]

# Model Compiling
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Model Training
# model.fit(train_ds, validation_data=valid_ds, callbacks=cbs, epochs=50)


# Specify Model Path
model_path = 'Vegetable-Classifier.keras'
model = load_model(model_path)

# Architecture
model.summary()


# Evaluation on test Set
model.evaluate(test_ds)

# Visualize Predictions
show_images(model=model, data=test_ds)

#==============================
# Load the image
img_path = 'pomidor.png'  # Path to the image
img = image.load_img(img_path, target_size=(256, 256))  # Resize to 256x256

# Convert image to numpy array
img_array = image.img_to_array(img)

# Expand dimensions to match the model input shape (batch_size, height, width, channels)
img_array = np.expand_dims(img_array, axis=0)

# Preprocess the image (apply ResNet50V2-specific preprocessing)
img_array = preprocess_input(img_array)

# Make prediction
prediction = model.predict(img_array)

# Decode the prediction
predicted_class_index = np.argmax(prediction, axis=1)
predicted_class = class_names[predicted_class_index[0]]

# Show the image and the prediction
plt.imshow(img)
plt.title(f"Predicted Class: {predicted_class}")
plt.axis('off')
plt.show()

print(f"Prediction: {predicted_class}, Probability: {prediction[0][predicted_class_index[0]]}")