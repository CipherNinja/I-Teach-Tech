import asyncio
import aiohttp

async def fetch_post(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
        session.close()
    except aiohttp.ClientError as err:
        print(err)


url_collection = [
    'https://jsonplaceholder.typicode.com/posts/1/comments',
    'https://jsonplaceholder.typicode.com/posts/2/comments',
    'https://jsonplaceholder.typicode.com/posts/3/comments'
]

async def main():
    response_json = [fetch_post(each_url) for each_url in url_collection]
    result = await asyncio.gather(*response_json,return_exceptions=True)
    print(result)

asyncio.run(main())