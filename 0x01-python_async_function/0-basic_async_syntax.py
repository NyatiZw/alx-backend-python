#!/usr/bin/env python3
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


async def main() -> None:
    """
    Main asynchronous function to run coroutine.
    """
    result = await wait_random()
    print(f"Waited for {result:2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
