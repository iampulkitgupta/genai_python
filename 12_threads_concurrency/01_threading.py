import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brew Chai for #{i}")
        time.sleep(2)


def main():
    print("Inside main")
    take_orders()
    brew_chai()


# Create threads

if "__name__" == "__main__":
    print("Dundder")
    main()

