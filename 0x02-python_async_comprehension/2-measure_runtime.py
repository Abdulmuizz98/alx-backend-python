#!/usr/bin/env python3
"""Contains the measure_runtime coroutine
"""

from asyncio import gather
import asyncio
import time

asy_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the total runtime of four async_comprehension
        routines in parallel
    """
    s = time.perf_counter()
    await gather(asy_c(), asy_c(), asy_c(), asy_c())
    elapsed = time.perf_counter() - s
    return elapsed
