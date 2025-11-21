snack = input("Enter your preferred snack: ").lower()
if not snack in ("cookies", "samosa"):
    print("Sorry we are serving onyl cookies and samosa only")
else:
    print("Your order is confirmed")
