import asyncio

async def brew_chai():
    print("Brewing Chai")
    await asyncio.sleep(5)
    print("Chai brewed")

asyncio.run(brew_chai())    