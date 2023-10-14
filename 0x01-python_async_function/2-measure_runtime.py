#!/usr/bin/env python3
"""
This module provides a function
to measure the average execution time for wait_n
"""


import asyncio
import time
from typing import Callable
from importlib import import_module


wait_n_module = import_module('1-concurrent_coroutines')
wait_n = wait_n_module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n.


    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay in seconds for each call.

    Returns:
        float: The average execution timme in seconds
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    avg_time = measure_time(n, max_delay)
    print(avg_time)
