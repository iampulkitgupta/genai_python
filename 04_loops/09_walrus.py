# value = 13
# remainder = value % 5

# if remainder:
#     print(f"{value} is not divisible by 5")


value = 13
if (remainder := value % 5):
    print(f"{value} is not divisible by 5")


available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your size: ")) in available_sizes:
#     print("Size is valid")
# else:
#     print("Invalid size")  

flavours = ["masala", "ginger", "lemon", "tulsi"]

print("Available flavours are: ")

while (flavour := input("Choose your flavour: ")) not in flavours:
    print("Invalid flavour")

print(f"You choose flavour {flavour}")
