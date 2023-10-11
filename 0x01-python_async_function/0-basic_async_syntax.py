#!/usr/bin/env python3
import random
import asyncio

""" asynchronous coroutine
    Args:
        max_delay: integer
        wait_random: integer

    Return: integer value
"""


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    result = await wait_random()
    print(f"Waited for {result:2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
