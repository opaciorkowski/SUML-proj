import streamlit as st
import base64
from recipe import Recipe

st.set_page_config(page_title="Recipes", page_icon="🍅", layout="wide")

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

set_png_as_page_bg('UI/img/veg_background4.jpg')

# Page title
st.header("Recipes", divider="red")
st.write("Check out our recipes!")

Recipe.load_recipes()
recipes = st.session_state["sorted_recipes"]

if "selected_recipe" not in st.session_state:
    st.session_state["selected_recipe"] = None

@st.dialog("Recipe details", width="large")
def open_recipe():
    selected = st.session_state["selected_recipe"]
    st.header(selected.title)
    st.image("UI/"+selected.image_path, caption=selected.title, use_container_width=True)
    st.write("### Description")
    st.write(selected.description)
    st.write("### Tags")
    st.write(", ".join(selected.tags))
    st.write("### Ingredients")
    for ingredient in selected.ingredients:
        st.write(f"- {ingredient}")
    st.write("### Instructions")
    for i, step in enumerate(selected.steps, start=1):
        st.write(f"{i}. {step}")
    st.session_state["selected_recipe"] = None

# Recipe layout
for i, recipe in enumerate(recipes):
    with st.container(border=True):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("UI/"+recipe.image_path, use_container_width=False)
        with col2:
            st.subheader(recipe.title)
            st.write(recipe.description)
            st.write("Tags: " + ", ".join(recipe.tags))

            # Button to view recipe details
            if st.button("View Details", key=f"view_{i}"):
                st.session_state["selected_recipe"] = recipe
                open_recipe()
