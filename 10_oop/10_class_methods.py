class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split(",")
        return cls(tea_type, sweetness, size)


chai_order_from_dict = ChaiOrder.from_dict({
    "tea_type": "Masala Chai",
    "sweetness": "Medium",
    "size": "Large",
})

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]

print(ChaiUtils.is_valid_size("Medium"))

chai_order_from_string = ChaiOrder.from_string("Masala Chai,Medium,Large")

print(chai_order_from_dict.__dict__)
print(chai_order_from_string.__str__)
