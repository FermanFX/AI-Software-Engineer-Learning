# aiohttp istifadə edin
# async with ClientSession yaradın
# hər URL üçün async request
# göndərin
# status code çap edin
# asyncio.gather ilə hamısını birlikdəişlədin
import asyncio
from aiohttp import ClientSession
async def print_status(url, session):
    async with session.get(url) as response:
        print(f"{url} status: {response.status}")

async def main():
    urls = [
        "https://example.com",
        "https://google.com",
        "https://github.com"
    ]
    async with ClientSession() as session:
        tasks = [print_status(url, session) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
