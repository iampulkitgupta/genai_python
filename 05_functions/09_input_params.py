# chai = "Ginger chai"

# def prepare_chai(order):
#     print(f"Preparing {order}")

# prepare_chai(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(f"Making chai with {tea}, {milk}, {sugar}")

make_chai("Ginger", "Cow", "Sugar")
make_chai(tea="Green", sugar="Medium", milk="No")


def special_chai(*args, **kwargs):
    print(args)
    enum = enumerate(args)
    print(list(enum))
    print(kwargs)

special_chai("Ginger", "Cow", "Sugar", tea="Green", sugar="Medium", milk="No")


# def chai_order(order=[]):
#     order.append("Chai")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    order.append("Chai")
    print(order)

chai_order()
chai_order()