import threading

chai_stock = 0

def restock_chai():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [threading.Thread(target=restock_chai) for _ in range(2)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]
    
print(chai_stock)