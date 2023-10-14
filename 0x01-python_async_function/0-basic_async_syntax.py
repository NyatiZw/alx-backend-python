#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine for waiting a random delay.
"""

import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    """
    asynchronous coroutine

    Args:
        max_delay: float

    Returns:
        float default value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    """
    Main asynchronous function to run coroutine.
    """
    max_delay = 5
    result = await wait_random(max_delay)
    print(f"Waited for {result:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
