ingredients = ["water", "milk", "ginger", "tea"]
print(id(ingredients))
print(f"Ingredients: {ingredients}")
ingredients.append("sugar")
print(f"Ingredients after adding sugar: {ingredients}")
print(id(ingredients))


spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(chai_ingredients)

chai_ingredients.insert(2, "tea")
print(chai_ingredients)

last_added = chai_ingredients.pop()
print(last_added)
print(chai_ingredients)

chai_ingredients.reverse()
print(chai_ingredients)

chai_ingredients.sort()
print(chai_ingredients)

sugar_level = [1, 2, 3, 4, 5]
print(max(sugar_level))
print(min(sugar_level))
print(sum(sugar_level))


base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid = base_liquid + extra_flavour
print(full_liquid)

strong_brew = ["black", "water"] * 3
print(strong_brew)

raw_spice = bytearray(b"CINNAMON")
new_spice = raw_spice.replace(b"CINNA", b"CARDA")
print(raw_spice)
print(new_spice)