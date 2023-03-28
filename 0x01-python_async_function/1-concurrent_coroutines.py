#!/usr/bin/env python3
"""
"""
import asyncio
from operator import itemgetter
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    """
    res = [max_delay] * n

    values = await asyncio.gather(*map(wait_random, res))
    sorted_values = [value for value, _ in sorted(
        zip(values, values), key=itemgetter(1)
        )]
    return sorted_values
    #  asyncio.run(wait_random(max_delay))
