# import threading

# counter = 0
# lock = threading.Lock()

# def increament():
#     global counter
#     for _ in range(100000):
#         with lock:
#             counter += 1

# threads = [threading.Thread(target=increament) for _ in range(10)]
# [t.start() for t in threads]
# [t.join() for t in threads]

# print(f"Final counter: {counter}")

import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100):
        # counter += 1
        # print(f"{threading.current_thread().name}, counter {counter}")
        with lock:
            counter += 1
            print(f"{threading.current_thread().name}, counter {counter}")

threads = [threading.Thread(target= increment, name=f"Thread-{i}") for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final Counter: {counter}")