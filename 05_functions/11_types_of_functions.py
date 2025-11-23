def pure_chai(cups):
    return cups * 10

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))
print(strong_chai)

