import aiohttp
import asyncio

async def fetch_async(session, url):
    async with session.get(url) as response:
            print("Async fetch completed")
            print("Status code: ", response.status)
            print("Content Type: ", response.headers["Content-Type"])
            # print("Content: ", await response.text())
            # return await response.text()

async def main():
    urls = [
        "https://httpbin.org/delay/3"       
    ] * 3

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]        
        await asyncio.gather(*tasks)
    
asyncio.run(main())
