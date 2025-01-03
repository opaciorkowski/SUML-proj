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

    def create_sample_recipes():
        recipes = []

        rec1 = Recipe("Everyday Salad", 
                    "Simple salad for everyday, great with every meal!",
                    "https://via.placeholder.com/150",
                    ["tomato", "cucumber", "onion", "salad"]
                    )
        recipes.append(rec1)

        rec2 = Recipe("Everyday Salad", 
                    "Simple salad for everyday, great with every meal!",
                    "https://via.placeholder.com/150",
                    ["spinach"]
                    )
        recipes.append(rec2)

        rec3 = Recipe("Everyday Salad", 
                    "Simple salad for everyday, great with every meal!",
                    "https://via.placeholder.com/150",
                    ["capsicum"]
                    )
        recipes.append(rec3)

        return recipes