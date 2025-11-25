class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def describe(self):
        print(f"This chai is {self.type} and size is {self.size}")


order_one = ChaiOrder("ginger", "150ml")
order_one.describe()


