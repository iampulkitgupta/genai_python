import threading
import time

def monitor_tea_temp():
    count = 0
    while True:      
        print("Monitoring tea temperature...")  
        time.sleep(5)        
        count += 1
        if count == 5:
            break

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main Program done")