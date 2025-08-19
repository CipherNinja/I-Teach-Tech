import asyncio
import aiohttp
from aiohttp import ClientSession
from colorama import Fore, Style

API_URL = "https://example.com/api/blogs"

blogs_to_create = [
    {"title": "Async in Python", "content": "Exploring asyncio and aiohttp."},
    {"title": "Data Pipelines", "content": "Building modular ETL flows."},
    {"title": "Network Graphs", "content": "Visualizing relationships with NetworkX."},
]

async def create_blog(session: ClientSession, blog_data: dict):
    try:
        async with session.post(API_URL, json=blog_data) as response:
            if response.status == 201:
                result = await response.json()
                print(f"{Fore.GREEN}✅ Created: {result.get('title', 'Untitled')}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Failed ({response.status}): {blog_data['title']}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.YELLOW}⚠️ Error: {e} for blog '{blog_data['title']}'{Style.RESET_ALL}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [create_blog(session, blog) for blog in blogs_to_create]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
