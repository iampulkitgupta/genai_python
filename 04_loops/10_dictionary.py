users = [
    {"id": 1, "total": 100, "coupon": "p20"},
    {"id": 2, "total": 200, "coupon": "f10"},
    {"id": 3, "total": 300, "coupon": "p40"},
    {"id": 4, "total": 400, "coupon": "p50"},
    {"id": 5, "total": 500, "coupon": "p60"},
]

discounts = {
    "p20": (0.2, 0),
    "f10": (0, 10),
    "p40": (0.4, 0),
    "p50": (0.5, 0),
    "p60": (0.6, 0),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    user["discount_percent"] = percent      
    user["discount_fixed"] = fixed
    user["discount_amount"] = user["total"] * percent + fixed

print(users)