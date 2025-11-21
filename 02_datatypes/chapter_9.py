essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(all_spices)

common_spices = essential_spices & optional_spices
print(common_spices)

only_in_essentials = essential_spices - optional_spices
print(only_in_essentials)

print(f"Is cloves in essential spices? {'cloves' in essential_spices}")