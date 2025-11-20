chai_type = "Ginger"
customer_name = "Priya"

print(f"{customer_name} ordered {chai_type} chai")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"Last Word: {chai_description[-4:]}")
print(f"Reverse String: {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(encoded_label)
decoded_label = encoded_label.decode("utf-8")
print(decoded_label)