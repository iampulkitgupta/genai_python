try:
    order_amount = int(input("Enter the Order amount: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

delivery_fees = 0 if order_amount > 300 else 30


print(f"Delivery fees: {delivery_fees}")