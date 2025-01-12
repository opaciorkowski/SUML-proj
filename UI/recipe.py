class Recipe:
    def __init__(self, title, description, image_path, tags):
        self.title = title
        self.description = description
        self.image_path = image_path
        self.tags = tags

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
            ["Broccoli"]  
        )
        recipes.append(rec1)

        rec2 = Recipe(
            "Creamy Pumpkin Soup",
            "A thick and flavorful pumpkin cream soup, perfect for chilly days.",
            "img/Creamy-pumpkin.jpg",  
            ["Pumpkin", "Tomato"]  
        )
        recipes.append(rec2)

        rec3 = Recipe(
            "Cucumber Tomato Salad",
            "A refreshing cucumber and tomato salad with onion and a light dressing.",
            "img/tomato-salad.jpg",  
            ["Cucumber", "Carrot", "Tomato"]  
        )
        recipes.append(rec3)

        rec4 = Recipe(
            "Brinjal Curry (Eggplant Curry)",
            "A traditional recipe for eggplant curry, full of Indian spices and flavors.",
            "img/Brinjal-Curry.jpg",  
            ["Brinjal"]  
        )
        recipes.append(rec4)

        rec5 = Recipe(
            "Carrot & Radish Pickle",
            "A slightly spicy and tangy recipe for pickled carrots and radishes. A great addition to main dishes.",
            "img/pickled.webp",  
            ["Carrot", "Radish"]  
        )
        recipes.append(rec5)

        rec6 = Recipe(
            "Papaya Smoothie",
            "An exotic papaya smoothie, perfect for breakfast or a healthy snack.",
            "img/papaya.jpg",  
            ["Papaya"]  
        )
        recipes.append(rec6)

        return recipes