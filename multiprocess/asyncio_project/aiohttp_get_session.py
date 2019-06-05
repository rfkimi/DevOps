#!/usr/bin/env python
# encoding: utf-8
import asyncio
import time
from aiohttp import ClientSession


tasks = []
url1 = "https://www.baidu.com/{}"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)
            print(time.time())


def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url1.format(i)))
        tasks.append(task)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))
