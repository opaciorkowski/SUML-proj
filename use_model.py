from tensorflow.keras.models import load_model
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Specify the directory used during training
trainpath = 'Vegetable Images/train'

# Get class labels in alphabetical order
labels = sorted(os.listdir(trainpath))

# Create a mapping from index to class name
labels_mapping = {index: label for index, label in enumerate(labels)}
print("Labels Mapping:", labels_mapping)

# Load the saved model
model = load_model("Vegetables_model.keras")

# Path to your image
image_path = "Tomato_je.jpg"

# Load the image using OpenCV
img = cv2.imread(image_path)

# Resize the image to 100x100
img_resized = cv2.resize(img, (100, 100))

# Convert BGR to RGB (if using OpenCV)
img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

# Normalize the image
img_normalized = img_resized / 255.0

# Add a batch dimension to the image
img_preprocessed = np.expand_dims(img_normalized, axis=0)

# Predict the class probabilities
predictions = model.predict(img_preprocessed)

# Get the class with the highest probability
predicted_class = np.argmax(predictions, axis=1)[0]
confidence = np.max(predictions)

# Map the predicted class index to the class label
predicted_label = labels[predicted_class]

print(f"Predicted Class: {predicted_label}")
print(f"Confidence: {confidence:.2f}")

plt.imshow(img_resized)
plt.title(f"Prediction: {predicted_label} (Confidence: {confidence:.2f})")
plt.axis('off')
plt.show()


