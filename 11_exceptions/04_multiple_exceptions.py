def process_order(item, quantity):
    try:
        price = {"masala": 30}[item]
        cost = price * quantity
        print(f"Cost of {quantity} {item} chai is {cost}")
    except:
        pass

process_order("masala", 20)