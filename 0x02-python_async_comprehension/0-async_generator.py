#!/usr/bin/env python3
"""Contains the async_generator coroutine
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ Corouting that loops 10 times, and generate random
        number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.random() * (10 - 0) + 0)
