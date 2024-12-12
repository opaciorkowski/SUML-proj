import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="Recipes",
    page_icon="🍅",
)

st.sidebar.header("Recipes")

# Helper function for text fading
def fade_text_style():
    st.markdown("""
    <style>
    .tile {
        height: 300px; /* Fixed height */
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
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
    .description::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 20px;
        background: linear-gradient(to bottom, transparent, white);
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

#TODO: add functionality
# Define tiles
tiles = [
    {"title": "Page 1", "image": "https://via.placeholder.com/150", "description": "This is a short description.", "page": "Page1"},
    {"title": "Page 2", "image": "https://via.placeholder.com/150", "description": "This is a much longer description that might get truncated if it exceeds the maximum height of the tile description box.", "page": "Page2"},
    {"title": "Page 3", "image": "https://via.placeholder.com/150", "description": "Another description with moderate length for this page.", "page": "Page3"}
]

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


