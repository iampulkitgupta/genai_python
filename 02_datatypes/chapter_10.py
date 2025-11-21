chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai Order: {chai_order}")

chai_receipe = {}
chai_receipe["base"] = "black_tea"
chai_receipe["liquid"] = "milk"
print(chai_receipe)

del chai_receipe["liquid"]
print(chai_receipe)


# print('base' in chai_receipe)

# print(f"Order details {chai_order.keys()}")
# print(f"Order details {chai_order.values()}")
# print(f"Order details {chai_order.items()}")

extra_spices = {"ginger": "1 tsp", "cardamom": "2 pods"}
chai_receipe.update(extra_spices)
print(chai_receipe)