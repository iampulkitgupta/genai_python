class InvalidChaiError(Exception): pass

def bill(flavor, quantity):
    menu = {"masala": 30, "green": 35, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Invalid flavor")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        print(f"Bill for {flavor} chai is {menu[flavor] * quantity}")
    except InvalidChaiError as e:
        print(e)
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for visiting")

bill("ginger", 2)
bill("ginger", "2")

