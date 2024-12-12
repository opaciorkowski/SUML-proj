import streamlit as st

st.set_page_config(
    page_title="Classifier",
    page_icon="🍅",
)

st.header("Vegetable Classifier", divider="red")
st.write("Upload an image of a vegetable, and the model will predict its class.")

st.sidebar.header("Classifier")
#TODO: add functionality
# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.write("")
    st.write("Processing...")

