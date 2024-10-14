#!/usr/bin/env python3
"""Wait a random amount of time."""


import asyncio
import random


async def wait_random(max_delay: int = 10.0) -> float:
    """Wait a random amount of time."""
    rand_i = random.uniform(0.0, max_delay)
    await asyncio.sleep(rand_i)
    return (rand_i)
