import streamlit as st

class Recipe:
    def __init__(self, title, description, image_path, tags, ingredients, steps):
        self.title = title
        self.description = description
        self.image_path = image_path
        self.tags = tags
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return f"{self.title} ({self.description}, {self.tags})"

    def add_tag(self, new_tag):
        self.tags.append(new_tag)

    @staticmethod
    def create_sample_recipes():
        recipes = []

        rec1 = Recipe(
            "Broccoli Stir-Fry",
            "A quick and healthy recipe for stir-fried broccoli with garlic and spices. Perfect as a side dish for dinner.",
            "img/stir-fry.jpg",  
            ["Broccoli", "capsicum"],
            ["For the sauce: water, soy sauce, honey, minced garlic, fresh ginger, black pepper, cornstarch",
             "olive oil", "broccoli", "cremini mushrooms", "bell pepper", "cooked rice"],
            ["Make the stir fry sauce by mixing together all of the sauce ingredients in a small bowl.",
            "Stir-fry the vegetables. First, heat the olive oil in a large skillet over medium-high heat. Then add the broccoli and mushrooms to the pan and cook, stirring often, for 4 minutes. Add the bell pepper and cook for 2-3 more minutes, until the veggies are crisp-tender.",
            "Add the sauce and cook for 1 minute, until the sauce thickens."
            ]
        )
        recipes.append(rec1)

        rec2 = Recipe(
            "Creamy Pumpkin Soup",
            "A thick and flavorful pumpkin cream soup, perfect for chilly days.",
            "img/Creamy-pumpkin.jpg",  
            ["Pumpkin", "Tomato"],
            ["1kg pumpkin, peeled and chopped", "2–3 teaspoons reduced-salt vegetable stock powder", "3 cups boiling water", "1 tablespoon olive oil", "1 medium brown onion, chopped", 
             "2 cloves garlic, crushed", "½ teaspoon ground cumin", "½ teaspoon ground nutmeg", "1 cup skim milk", "¼ cup reduced-fat sour cream, to serve", "4 tablespoons chopped roasted nuts and seeds"],
            ["In a large heavy-based pan, place pumpkin, stock powder and boiling water. Cover and bring to the boil. Reduce heat and simmer for 15–20 minutes, or until softened.",
            "Meanwhile, heat olive oil in a saucepan over medium-high. Sauté onion and garlic for 3–4 minutes, or until onion is softened. Add cumin and nutmeg and cook for 30 seconds. Add milk and season with cracked black pepper.",
            "Remove pumpkin from heat. Pour milk mixture into pumpkin mixture. Using a stick blender, carefully blend until smooth. Return to stove and reheat, if needed.",
            "Divide soup among four bowls. Swirl over sour cream and scatter with chopped nuts and seeds."]  
        )
        recipes.append(rec2)

        rec3 = Recipe(
            "Cucumber Tomato Salad",
            "A refreshing cucumber and tomato salad with onion and a light dressing.",
            "img/tomato-salad.jpg",  
            ["Cucumber", "Carrot", "Tomato"],
            ["cucumber", "tomato", "carrot", "red onion", "herbs", "olive oil", "vinegar", "mustard", "oregano", "salt", "pepper"],
            ["Slice fresh vegetables and place them in a bowl.",
            "In a separate bowl, add the ingredients for the herb dressing and mix well.",
            "Pour the dressing over the top of the vegetables, toss to mix"]
        )
        recipes.append(rec3)

        rec4 = Recipe(
            "Brinjal Curry (Eggplant Curry)",
            "A traditional recipe for eggplant curry, full of Indian spices and flavors.",
            "img/Brinjal-Curry.jpg",  
            ["Brinjal"],
            ["brinjal", "water", "onion", "guntur red chilli", "bydgi red chilli", "coconut", "roasted chana dal", "peanuts", "garlic",
             "jaggery", "coriander leaves", "tamarind", "coriander seeds", "sesame seeds", "cumin seeds", "mustard seeds", "oil", "salt"] ,
            ["Add all the paste ingredients except the water to the chutney jar of a mixer. Grind into a fine paste.",
             "Add water little by little as you grind it. Ensure the paste is smooth and free of lumps. Keep aside.",
             "Make an X-shaped cut on the bottom of a brinjal. The cut should be deep enough to slightly open up the brinjal.",
             "Stuff the opening with the prepared paste. Repeat for the remaining brinjal and set it aside. Do not discard the excess paste.",
             "Add oil to a flat bottomed kadai or sauteuse pan. Allow the oil to heat on a high flame. Add mustard seeds and allow them to splutter.",
             "Add the prepared brinjal to the pan. Spread them out as much as possible and shallow fry for 2-3 minutes on each side. Use tongs to turn the brinjals.",
             "Add sliced onion and stir. Saute for 3-4 minutes.",
             "Add the remaining paste and mix to combine. Fry for 3 minutes.",
             "Add 1 cup of water and mix.",
             "Cover the pan with a lid and cook on medium-low heat for 25-30 minutes or until the brinjal is cooked. It may take longer to cook depending on the size of the brinjal.",
             "Add the remaining half cup of water little by little to adjust the consistency of the gravy as desired. Serve hot along with rice and ghee or jowar rotis!"] 
        )
        recipes.append(rec4)

        rec5 = Recipe(
            "Carrot & Radish Pickle",
            "A slightly spicy and tangy recipe for pickled carrots and radishes. A great addition to main dishes.",
            "img/pickled.webp",  
            ["Carrot", "Radish"],
            ["carrot", "radish", "vinegar", "sugar", "salt"],
            ["Dissolve the sugar and salt in a large bowl with 1 1/2 cups of boiling water.",
             "Add the vinegar and vegetables and set aside for at least 2 hours or until the vegetables become a little floppy."] 
        )
        recipes.append(rec5)

        rec6 = Recipe(
            "Papaya Smoothie",
            "An exotic papaya smoothie, perfect for breakfast or a healthy snack.",
            "img/papaya.jpg",  
            ["Papaya"],
            ["1/2 medium papaya", " 1 large ripe banana (preferably frozen)", "1 1/2 cup almond milk", "1/4 to 1/2 tsp ground turmeric",
             "1 tbsp lemon or lime juice", "2 tbsp honey", "1 cup ice"],
            ["Place all ingredients on a blender and blend until smooth.",
            "Pour into two glasses and serve."]  
        )
        recipes.append(rec6)

        return recipes
    
    def load_recipes():
        if "recipes" not in st.session_state:
            st.session_state["recipes"] = Recipe.create_sample_recipes()
        if "sorted_recipes" not in st.session_state:
            st.session_state["sorted_recipes"] = st.session_state["recipes"]
            