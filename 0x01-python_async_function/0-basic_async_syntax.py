#!/usr/bin/env python3
""" Contains the function wait_random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Async wait for a random delay from 0 - max_delay
    """
    time = random.random() * (max_delay - 0) + 0
    await asyncio.sleep(time)
    return time
