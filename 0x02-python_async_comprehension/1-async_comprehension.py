#!/usr/bin/env python3
"""Contains the async_comprehension coroutine
"""

import asyncio
from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ use async comprehension to return yields of async_generator
    """
    return [i async for i in async_generator()]
