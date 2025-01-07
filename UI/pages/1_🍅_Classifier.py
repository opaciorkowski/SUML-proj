import streamlit as st
import base64
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Classifier",
    page_icon="🍅",
)

st.header("Vegetable Classifier", divider="red")
st.write("Upload an image of a vegetable, and the model will predict its class.")

st.sidebar.header("Classifier")

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

set_png_as_page_bg('img/veg_background4.jpg')

def search_for_recipe(veg_list):
    veg_list = [veg.lower() for veg in veg_list]
    recipes = st.session_state["recipes"]
    scores = {}

    for rec in recipes:
        scores[rec] = 0
        for tag in rec.tags:
            if tag in veg_list:
                scores[rec] += 1

    result = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    return result


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
    model = load_model("../Vegetables_model.keras")
    return model

model = load_vegetable_model()

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


if "veg_list" not in st.session_state:
    st.session_state["veg_list"] = []


col1, col2, col3, col4= st.columns([2, 1, 1, 2])
message_container = st.container()

with col2:
    but1 = st.button("Add item")
    if but1:
        if uploaded_file is None:
            with message_container:
                st.error("Please make a prediction first!")
        else: 
            st.session_state["veg_list"].append(predicted_label)
            with message_container:
                st.success(f"{predicted_label} added to list!")
with col3:
    but2 = st.button("Find recipe")
    if but2:
        if len(st.session_state["veg_list"]) == 0:
            with message_container:
                st.error("Please add at least 1 item!")
        else:
            st.session_state["sorted_recipes"] = search_for_recipe(st.session_state["veg_list"])
            st.switch_page("pages/2_🍽_Recipes.py")
