def serve_chai(order):
    try:
        print(f"Preparing {order}")
        if order == "unknown":
            raise ValueError("We don't know the flavor")
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for visiting")

serve_chai("Ginger")
serve_chai("unknown")