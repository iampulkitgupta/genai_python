masala_spices = ("cumin", "coriander", "turmeric")
print(masala_spices)

print(id(masala_spices))

masala_spices += ("cardamom", "cinnamon")
print(masala_spices)
print(id(masala_spices))

#membership

print(f"Is cardamom in masala_spices: {'cardamom' in masala_spices}")
print(f"Is cinnamon in masala_spices: {'cinnamon' in masala_spices}")
