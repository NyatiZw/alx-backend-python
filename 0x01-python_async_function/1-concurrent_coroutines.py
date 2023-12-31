#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine for waiting a random delay.
"""


import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine

    Args:
        max_delay (float): The maximum delay in seconds

    Returns:
        float: The actual delay in seconds
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` n times with the specified `max_delay`.

    Args:
        n (int): The number of times to run `wait_random`.
        max_delay (float): The maximum delay in seconds for each call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays: List[float] = [0] * n

    async def run_wait_random(i: int):
        delay = await wait_random(max_delay)
        delays[i] = delay

    tasks = [run_wait_random(i) for i in range(n)]
    await asyncio.gather(*tasks)
    return delays


async def main():
    n = 5
    max_delay = 5.0
    result = await wait_n(n, max_delay)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
