import streamlit as st

st.set_page_config(
    page_title="Welcome to Vegetable Classifier",
    page_icon="🍅",
)

st.sidebar.header("Welcome Page")

st.title("Welcome to Vegetable Classifier!🍅")


st.header("What is this", divider="red")
st.write(""+
         "Vegatable Classifier is an app made to easily recognize images of fruit "+
         "and vegetables."+
         "")


st.header("Get to know our classifier", divider="red")
st.markdown(f"""
            Our classifier is trained on a large amount of images and provides quick 
            recognition of fruit and vegetables. You can try it yourself in the 
            st.page_link("pages/1_🍅_Classifier.py") tab
            """, unsafe_allow_html=True)




st.header("Explore our recipes", divider="red")
st.markdown(f"""
            You can explore our recipes
            """, unsafe_allow_html=True)



st.header("Read about the authors", divider="red")
st.markdown(f"""
            Get to know us better 
            """, unsafe_allow_html=True)



st.header("Documentation", divider="red")
st.markdown(f"""
            You can read our documentation here
            """, unsafe_allow_html=True)
#TODO: add info