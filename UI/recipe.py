import streamlit as st

class Recipe:
    def __init__(self, title, description, image, tags):
        self.title = title
        self.description = description
        self.image = image
        self.tags = tags

    def __str__(self):
        return f"{self.title} ({self.description}, {self.tags})"

    def add_tag(self, new_tag):
        self.tags.append(new_tag)

    def load_recipes():
        if "recipes" not in st.session_state:
            #TODO Replace this with loading from a db or file
            st.session_state["recipes"] = [
            Recipe("Everyday Salad", 
                    "Simple salad for everyday, great with every meal!",
                    "https://via.placeholder.com/150",
                    ["tomato", "cucumber", "onion", "salad"]
            ),
            Recipe("Everyday Salad", 
                    "Simple salad for everyday, great with every meal!",
                    "https://via.placeholder.com/150",
                    ["spinach"]
            ),
            Recipe("Everyday Salad", 
                    "Simple salad for everyday, great with every meal!",
                    "https://via.placeholder.com/150",
                    ["capsicum"]
            )
        ]
        if "sorted_recipes" not in st.session_state:
            st.session_state["sorted_recipes"] = st.session_state["recipes"]