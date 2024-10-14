#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait up to max_delay seconds and then return length of delay."""
    delay = random.uniform(1.0, max_delay)
    await asyncio.sleep(delay)
    return delay
