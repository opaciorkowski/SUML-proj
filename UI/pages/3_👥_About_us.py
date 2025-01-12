import streamlit as st
from PIL import Image, ImageDraw
import base64

st.set_page_config(
    page_title="About us",
    page_icon="🍅",
)

st.header("About us", divider="red")
st.write("Meet the authors behind this app!")

st.sidebar.header("About us")
#TODO: add info


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


def make_circle(image_path):
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    img = img.crop((0, 0, size, size))
    img.putalpha(mask)
    return img

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    circular_image = make_circle("img/Oskar.png")
    st.image(circular_image, caption="Oskar Paciorkowski", use_container_width=True)

with col2:
    circular_image = make_circle("img/Kuba.jpg")
    st.image(circular_image, caption="Jakub Wójcik", use_container_width=True)

with col3:
    circular_image = make_circle("img/Kinga.png")
    st.image(circular_image, caption="Kinga Mendyk", use_container_width=True)

