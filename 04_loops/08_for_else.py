staff = [("Amit", 16), ("Advik", 20), ("Pulkit", 17), ("Kajal", 16)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible for voting")
        break
    else:
        print(f"{name} is not eligible for voting")
else:
    print("All staff members have been checked")    