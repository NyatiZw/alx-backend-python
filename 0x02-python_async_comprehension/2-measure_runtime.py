#!/usr/bin/env python3
import asyncio
from time import perf_counter
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime


if __name__ == "__main__":
    total_runtime = asyncio.run(measure_runtime())
    print(f"{total_runtime}")
