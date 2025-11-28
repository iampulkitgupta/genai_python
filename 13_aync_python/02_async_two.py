import asyncio
import time

async def brew_chai(name):
    print(f"Brewing Chai for {name}")
    # await asyncio.sleep(5)
    time.sleep(5)
    print(f"Chai brewed for {name}")

async def main():
    await asyncio.gather(
        brew_chai("John"), 
        brew_chai("Jane"),
    )

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Total time: {end - start}")

