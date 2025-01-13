import streamlit as st
import base64

st.set_page_config(
    page_title="Documentation",
    page_icon="🍅",
)

# Set background image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('UI/img/veg_background4.jpg')

st.header("Vegetable and Fruit Classifier Documentation", divider="red")

st.sidebar.header("Contents")
st.sidebar.markdown("""
- [Introduction](#introduction)
- [Project Goal](#project-goal)
- [Dataset Description](#dataset-description)
- [Model Architecture](#model-architecture)
- [Application Description](#application-description)
""")

st.subheader("Introduction")
st.write("""This is the documentation for the **Vegetable and Fruit Classifier**, an application that leverages machine learning to classify vegetables and fruits and provide recipe recommendations based on the classified ingredients.""")

st.subheader("Project Goal")
st.write("""The goal of the project is to build an application that recognizes vegetables and fruits from images and suggests recipes containing these ingredients. The application is tailored to users in regions like India and Bangladesh due to the dataset's origin but can potentially be expanded globally.""")

st.subheader("Dataset Description")
st.write("""The model uses the **Vegetable Image Dataset** from Kaggle. The dataset contains images of various vegetables and fruits collected from farms and markets for project purposes.
- [Dataset on Kaggle](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

Data preprocessing steps included:
- Resizing all images to 100x100 pixels.
- Normalizing pixel values to the [0, 1] range.
- Splitting data into training (70%), validation (15%), and testing (15%) sets.
""")

st.subheader("Model Architecture")
st.write("""The model is a Convolutional Neural Network (CNN) designed to classify images into 10 categories:
- **Bean**
- **Cabbage**
- **Capsicum**
- **Carrot**
- **Cucumber**
- **Papaya**
- **Potato**
- **Pumpkin**
- **Radish**
- **Tomato**

### Key Features:
1. **Conv2D Layers**: Extract patterns and features like shapes and textures.
2. **MaxPooling Layers**: Reduce dimensions while retaining important features.
3. **Flatten Layer**: Prepare data for fully connected layers.
4. **Dense Layers**: Classify features into specific categories.

The model achieved an accuracy of **96.77%** on validation data and **96.60%** on test data.
""")

st.subheader("Application Description")
st.write("""The application was developed using the following technologies:
- **Python** for backend development.
- **Streamlit** for building an interactive user interface.
- **TensorFlow/Keras** for machine learning.
- **OpenCV** for image processing.

### Key Features:
- Upload an image for classification.
- View classification results and model confidence.
- Add ingredients to a list and find recipes containing them.
- Recipe display with detailed preparation steps and ingredients.
""")

# Footer
st.write("""---
Documentation created by: Kinga Mendyk, Oskar Paciorkowski, Jakub Wójcik
""")
