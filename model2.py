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
# Specify Model Path
model_path = 'Vegetables_model.keras'
model = load_model(model_path)

# Architecture
model.summary()


# # Evaluation on test Set
# model.evaluate(test_ds)

# # Visualize Predictions
# show_images(model=model, data=test_ds)

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