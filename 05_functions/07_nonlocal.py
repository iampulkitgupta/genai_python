chai_type = "Plain"


def update_order():
    chai_type = "Elaichi"
    print(f"Inside function {chai_type}")
    def kitchen():  
        nonlocal chai_type      
        chai_type = "Masala"
        print(f"Inside Inside kitchen {chai_type}")
    print(f"Outside before function {chai_type}")
    kitchen()
    print(f"Outside after function {chai_type}")

update_order()  
print(chai_type)