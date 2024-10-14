#!/usr/bin/env python3
"""Measure the average time."""


import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay):
    """Measure time."""
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
