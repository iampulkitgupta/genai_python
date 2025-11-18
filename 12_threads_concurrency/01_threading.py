import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brew Chai for #{i}")
        time.sleep(3)


# def main():    
#     start = time.time()
#     take_orders()
#     brew_chai()
#     end = time.time()
#     print("Total time taken: ", end - start, "seconds")

# if __name__ == "__main__":    
#     main()

# Create threads
start = time.time()
order_thread = threading.Thread(target= take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print("Done")
end = time.time()

print("Total time taken: ", end - start, "seconds")
