def infinite_chai():
    count = 1
    while True:
        yield f"Masala Chai {count}"
        count += 1

chai = infinite_chai()

for _ in range(5):
    print(next(chai))
