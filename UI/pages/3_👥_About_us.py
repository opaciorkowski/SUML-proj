import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(
    page_title="About us",
    page_icon="🍅",
)

st.header("About us", divider="red")
st.write("Meet the authors behind this app!")

st.sidebar.header("About us")
#TODO: add info


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
    circular_image = make_circle("img/person.png")
    st.image(circular_image, caption="Oskar Paciorkowski", use_container_width=True)

with col2:
    circular_image = make_circle("img/person.png")
    st.image(circular_image, caption="Jakub Wójcik", use_container_width=True)

with col3:
    circular_image = make_circle("img/person.png")
    st.image(circular_image, caption="Kinga Mendyk", use_container_width=True)

