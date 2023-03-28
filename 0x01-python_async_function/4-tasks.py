#!/usr/bin/env python3
"""Contains the function task_wait_random
"""
import asyncio
import time
from operator import itemgetter
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function that creates an async function
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function that executes multiple coroutines at the
        same time with async
    """
    res = [max_delay] * n

    values = await asyncio.gather(*map(task_wait_random, res))
    sorted_values = [value for value, _ in sorted(
        zip(values, values), key=itemgetter(1)
        )]
    return sorted_values
