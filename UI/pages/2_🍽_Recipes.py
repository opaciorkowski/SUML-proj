import streamlit as st
from recipe import Recipe

st.set_page_config(page_title="Recipes", page_icon="🍅", layout="wide")

# Add custom styles
def add_custom_styles():
    st.markdown("""
    <style>
    .recipe-card {
        border-radius: 8px;
        text-align: center;
        transition: transform 0.2s ease-in-out;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 10px;
        margin: 10px; 
    }
    .recipe-card:hover {
        transform: scale(1.05);
    }
    .recipe-card img {
        width: 200px; 
        height: auto; 
        object-fit: cover; 
        border-radius: 5px;
        cursor: pointer; 
    }
    </style>
    """, unsafe_allow_html=True)

add_custom_styles()

# Download recipes
recipes = Recipe.create_sample_recipes()

cols_per_row = 3
cols = st.columns(cols_per_row)

if "selected_recipe" not in st.session_state:
    st.session_state["selected_recipe"] = None

for idx, recipe in enumerate(recipes):
    col = cols[idx % cols_per_row]
    
    with col:
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        
        if st.button(recipe.title, key=f"button_{idx}"):
            st.session_state["selected_recipe"] = recipe  
        st.image(recipe.image_path, width=200, use_container_width=False)  
        
        st.markdown('</div>', unsafe_allow_html=True)

# Accurate informations on recipe
if st.session_state["selected_recipe"]:
    selected_recipe = st.session_state["selected_recipe"]
    
    st.markdown("<hr>", unsafe_allow_html=True)  
    with st.container():
        
        st.subheader(selected_recipe.title)
        st.image(selected_recipe.image_path)
        st.write(selected_recipe.description)
        
        if selected_recipe.tags:
            st.write("Tags:", ', '.join(selected_recipe.tags))
        
        if st.button("Close"):
            st.session_state["selected_recipe"] = None 
