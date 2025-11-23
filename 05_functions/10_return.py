def make_chai():
    return "Chai"

# print(make_chai())

def idle_chaiwala():
    pass

print(idle_chaiwala())


def sold_cups():
    return 10

total = sold_cups() 
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Out of stock"
    elif cups_left < 5:
        return "Low stock"
    else:
        return "In stock"    
    
print(chai_status(4))

def chai_report():
    return 100, 120

print(chai_report())