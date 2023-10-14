#!/usr/bin/env python3
"""
Function that returns a asyncio.Task
"""


import asyncio
from importlib import import_module
basic_async_syntax = import_module('0-basic_async_syntax')


wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that waits for a random delay

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    max_delay = 5
    task = task_wait_random(max_delay)
    asyncio.run(task)
