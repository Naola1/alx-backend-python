#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay and returns the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The actual delay time in seconds.

    Example:
        >>> import asyncio
        >>> delay = asyncio.run(wait_random(5))
        >>> print(f"Waited for {delay} seconds")
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
