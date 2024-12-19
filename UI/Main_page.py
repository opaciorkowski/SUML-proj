import streamlit as st
import base64

st.set_page_config(
    page_title="Welcome to Vegetable Classifier",
    page_icon="🍅",
)

st.sidebar.header("Welcome Page")

st.title("Welcome to Vegetable Classifier!🍅")

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
    background-position: center; /* Keeps the image centered */
    background-attachment: fixed; /* Prevents image from zooming in or moving with scroll */
    background-repeat: no-repeat; /* Avoids repeating the image */
    min-height: 100vh; 
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('img/veg_background4.jpg')


st.header("What is this", divider="red")
st.markdown(f"""
            Vegatable Classifier is an app made to easily recognize images of fruit
            and vegetables. You can upload an image and it will predict what kind of 
            produce it is. If you'd like, the model will reccomend you recipes based 
            on the provided images.
            """, unsafe_allow_html=True)


classifier_page = "Classifier"
st.header(f"Get to know our classifier", divider="red")
st.page_link("pages/1_🍅_Classifier.py")
st.markdown(f"""
            Our classifier is trained on a large amount of images and provides quick 
            recognition of fruit and vegetables. You can try it yourself in the 
            <a href="{classifier_page}" target="_self">🍅Classifier tab</a>.
            """, unsafe_allow_html=True)



recipe_page = "Recipes"
st.header("Explore our recipes", divider="red")
st.page_link("pages/2_🍽_Recipes.py")
st.markdown(f"""
            You can explore our recipes that we have prepared for you. Let the
            model know which ingredients you have and read the most accurate 
            recipe for you. You can also see all the recipes in our
            <a href="{recipe_page}" target="_self">🍽Recipes tab</a>. 
            """, unsafe_allow_html=True)


author_page = "About_us"
st.header("Read about the authors", divider="red")
st.page_link("pages/3_👥_About_us.py")
st.markdown(f"""
            Get to know us better! You can read about our team in the 
            <a href="{author_page}" target="_self">👥About us tab</a>. 
            """, unsafe_allow_html=True)


docs_page = "Documentation"
st.header("Documentation", divider="red")
st.page_link("pages/4_📄_Documentation.py")
st.markdown(f"""
            You can read our documentation in the
            <a href="{docs_page}" target="_self">📄Documentation tab</a>.
            """, unsafe_allow_html=True)
