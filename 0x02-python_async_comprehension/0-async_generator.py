#!/usr/bin/env python3
"""Coroutine that loops 10 times."""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that will loop 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
