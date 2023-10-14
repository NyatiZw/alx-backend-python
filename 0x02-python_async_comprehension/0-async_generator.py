#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncIterator

"""
This module defines an async generator coroutine that
yields random numbers between 0 and 10
with a 1-second delay betwen each yield
"""


async def async_generator() -> AsyncIterator[int]:
    """
    Asynchronous generator that yields random numbers
    between 0 and 10

    Yields:
        int: A random number between 0 and 10.

    Example:
        async for number in async_generator():
            print(f"Generated: {number}")
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

    async def main() -> None:
        """
        Example usage to consume values
        """
        async for number in async_generator():
            print(f"{number}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
