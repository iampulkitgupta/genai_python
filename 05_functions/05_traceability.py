def add_vat(price, vat_rate):
    return price + ((price * vat_rate) / 100)

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 20)
    print(f"Original Price is {price}, Final amount is {final_amount}" )