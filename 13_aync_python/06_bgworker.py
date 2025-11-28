import asyncio
import threading
import time

def bg_worker():
    while True:
        time.sleep(1)
        print("Background worker is running...")

async def fetch_orders():
    await asyncio.sleep(5)
    print("Orders fetched")

threading.Thread(target=bg_worker, daemon=True).start()

asyncio.run(fetch_orders())

