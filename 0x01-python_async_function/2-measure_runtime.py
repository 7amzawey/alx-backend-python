#!/usr/bin/env python3
"""Measure the average time."""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure time."""
    start_time = time.time()
    await asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
