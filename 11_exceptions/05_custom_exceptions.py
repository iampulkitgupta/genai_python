def brew_chai(flavor):
    try:
        if flavor not in ["masala", "ginger", "elaichi"]:
            raise ValueError("Invalid flavor")
        print(f"Brewing {flavor} chai...")
    except ValueError as e:
        print(e)

brew_chai("green")