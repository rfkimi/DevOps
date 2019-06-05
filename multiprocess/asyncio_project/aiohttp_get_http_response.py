#!/usr/bin/env python
# encoding: utf-8
import asyncio
import time
from aiohttp import ClientSession

url1 = "https://www.baidu.com/{}"


async def get_response(url, semaphore):
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url) as response:
                print(time.time())
                return await response.read()


async def run():
    semaphore = asyncio.Semaphore(500)  # limit max number of async
    to_get = [get_response(url1.format(i), semaphore) for i in range(1000)]  # max number of tasks
    await asyncio.wait(to_get)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()

