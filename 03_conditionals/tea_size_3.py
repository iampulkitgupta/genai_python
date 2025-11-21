cup_size = input("Which cup of tea do you require? ").lower()

if cup_size == "small":
    print(f"{cup_size} cup of tea is of Rs10")
elif cup_size == "medium":
    print(f"{cup_size} cup of tea is of Rs15")
elif cup_size == "large":
    print(f"{cup_size} cup of tea is of Rs20")
else:
    print("Unknown cup size")
