def process_order(item, quantity):
    try:
        price = {"masala": 30, "green": 35}[item]
        cost = price * quantity
        print(f"Cost of {quantity} {item} chai is {cost}")
    except:
        print("Sorry chai not on menu")

process_order("masala", 20)
process_order("green", 20)
process_order("ginger", 20)