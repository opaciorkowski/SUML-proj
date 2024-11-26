import streamlit as st
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Static Labels Mapping
labels_mapping = {
    0: 'Bean',
    1: 'Bitter_Gourd',
    2: 'Bottle_Gourd',
    3: 'Brinjal',
    4: 'Broccoli',
    5: 'Cabbage',
    6: 'Capsicum',
    7: 'Carrot',
    8: 'Cauliflower',
    9: 'Cucumber',
    10: 'Papaya',
    11: 'Potato',
    12: 'Pumpkin',
    13: 'Radish',
    14: 'Tomato'
}

# Load the saved model
@st.cache_resource
def load_vegetable_model():
    model = load_model("Vegetables_model.keras")
    return model

model = load_vegetable_model()

# Streamlit app configuration
st.title("Vegetable Classifier")
st.write("Upload an image of a vegetable, and the model will predict its class.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.write("")
    st.write("Processing...")

    # Read and preprocess the image
    img = Image.open(uploaded_file).convert("RGB")
    img_resized = img.resize((100, 100))  # Resize to model's input size
    img_array = np.array(img_resized) / 255.0  # Normalize the image
    img_preprocessed = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict the class probabilities
    predictions = model.predict(img_preprocessed)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    # Map the predicted class index to the class label
    predicted_label = labels_mapping[predicted_class]

    # Display the prediction
    st.write(f"**Predicted Class:** {predicted_label}")
    st.write(f"**Confidence:** {confidence:.2f}")

    # Show the uploaded image with prediction
    st.image(img_resized, caption=f"Prediction: {predicted_label} (Confidence: {confidence:.2f})", use_container_width=True)
