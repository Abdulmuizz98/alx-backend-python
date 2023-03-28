#!/usr/bin/env python3
"""Contains the measure_runtime coroutine
"""

import asyncio
import time

ac = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the total runtime of four async_comprehension
        routines in parallel
    """
    s = time.perf_counter()
    await asyncio.gather(ac(), ac(), ac(), ac())
    elapsed = time.perf_counter() - s
    return elapsed
