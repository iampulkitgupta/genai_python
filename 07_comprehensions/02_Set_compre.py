menu = ("chai", "samosa", "biryani", "samosa chaat", "samosa")

samosa = {item for item in menu if "samosa" in item}
print(samosa)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "cinnamon", "cloves", "fennel", "green cardamom", "ginger", "nutmeg", "pepper", "star anise", "vanilla bean"],
    "Elaichi Chai": ["ginger", "cardamom", "cinnamon", "cloves", "green cardamom", "ginger", "nutmeg", "pepper", "star anise", "vanilla bean"],
    "Spicy Chai": ["ginger", "cardamom", "cinnamon", "clove"],
}

unique_spices = {spice for recipe in recipes.values() for spice in recipe}
print(unique_spices)    