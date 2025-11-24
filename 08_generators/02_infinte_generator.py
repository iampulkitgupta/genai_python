def infinite_chai():
    count = 1
    while True:
        yield f"Masala Chai {count}"
        count += 1

chai = infinite_chai()

print(next(chai))
print(next(chai))
chai.close()
print(next(chai))

# for _ in range(5):
    # print(next(chai))
