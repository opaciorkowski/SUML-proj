import streamlit as st
import base64

st.set_page_config(
    page_title="Documntation",
    page_icon="🍅",
)

st.header("Documentation", divider="red")
st.write("Read")

st.sidebar.header("Documentation")
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

set_png_as_page_bg('UI/img/veg_background4.jpg')