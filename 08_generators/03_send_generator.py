def chai_customer():
    print("Customer: Hi, can I have a Masala Chai?")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield

chai_customer = chai_customer()
next(chai_customer)

chai_customer.send("Masala Chai")
chai_customer.send("Elaichi Chai")

