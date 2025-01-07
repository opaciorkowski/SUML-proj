import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header
import base64
from recipe import Recipe

st.set_page_config(
    page_title="Recipes",
    page_icon="🍅",
)

st.sidebar.header("Recipes")

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

# Helper function for text fading
def fade_text_style():
    st.markdown("""
    <style>
    .tile {
        height: 300px;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 4px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
        overflow: hidden;
        position: relative;
    }
    .tile:hover {
        transform: scale(1.05);
    }
    .description {
        max-height: 60px;
        overflow: hidden;
        text-overflow: ellipsis;
        position: relative;
    }
    .clickable {
        text-decoration: none;
        color: inherit;
    }
    </style>
    """, unsafe_allow_html=True)

# Add styles
fade_text_style()

# Page title
st.header("Recipes", divider="red")
st.write("Check out our recipes!")

Recipe.load_recipes()
recipes = st.session_state["sorted_recipes"]


# Define tiles
tiles = []
for rec in recipes:
    tiles.append({"title": rec.title, "image": rec.image, "description": rec.description, "page": None})


# Grid layout
cols = st.columns(3) 
for i, tile in enumerate(tiles):
    with cols[i % 3]:
        # Tile Content
        st.markdown(f"""
        <div class="tile">
            <a href="?page={tile['page']}" class="clickable">
                <img src="{tile['image']}" alt="{tile['title']}" style="width: 100%; border-radius: 5px;">
            </a>
            <h4>{tile['title']}</h4>
            <div class="description">{tile['description']}</div>
        </div>
        """, unsafe_allow_html=True)

# Subpage Navigation
query_params = st.query_params
if "page" in query_params:
    page = query_params["page"][0]
    if page == "Page1":
        st.write("Welcome to Page 1!")
    elif page == "Page2":
        st.write("Welcome to Page 2!")
    elif page == "Page3":
        st.write("Welcome to Page 3!")


