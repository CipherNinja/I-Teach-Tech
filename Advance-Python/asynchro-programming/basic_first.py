import asyncio
import aiohttp
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        # print(session)
        async with session.get(url) as response:
            # print(response)
            if response.status >= 200:
                return await response.json()
            raise ValueError(f"Failed to fetch url: {url}")
        

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2"
    ]

    tasks = [
        fetch_url(url) for url in urls
    ]

    results = await asyncio.gather(*tasks)
    for response in results:
        print(f"response: {response['title']}")

asyncio.run(main())
