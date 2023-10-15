#!/usr/bin/env python3
"""
Coroutine using async comprehension
"""


import asyncio
from typing import List
from random import uniform


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers
    """
    result = [number async for number in async_generator()]
    return result

async def main():
    random_numbers = await async_comprehension()
    print(random_numbers)


if __name__ == "__main__":
    asyncio.run(main())
