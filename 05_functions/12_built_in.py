def chai_flavours(flavour="masala"):
    """This function returns the flavour of chai"""
    return flavour

print(chai_flavours.__doc__)
print(chai_flavours.__name__)
print(chai_flavours.__code__)
print(chai_flavours.__defaults__)



def generate_bill(chai=0, samosa=0):
    """This function generates the bill for chai and samosa
    :param chai: Number of chai
    :param samosa: Number of samosa
    :return: Total bill
    """
    return chai * 20 + samosa * 10

print(generate_bill.__doc__)
print(generate_bill.__name__)
print(generate_bill.__code__)
print(generate_bill.__defaults__)
print(generate_bill.__annotations__)