import asyncio
import aiohttp
import time
import json


day_dict = {}

base = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="
companies = ["aapl", 'akza']
endpoint = "&interval=1min&apikey=KJF901I3K0O8W3ZX"

urls = [f"{base}{company}{endpoint}" for company in companies]

print(urls)

def parse_response(data):
    pass

async def scrape(urls):
    async with aiohttp.ClientSession() as session:
        while True:
            for url in urls:
                async with session.get(url) as resp:
                    print(resp.status)
                    print (f'received {url}')
                    print(await resp.text())
            time.sleep(5)            




futures = [scrape(urls)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))