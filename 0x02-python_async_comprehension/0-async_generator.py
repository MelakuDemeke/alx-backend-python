#!/usr/bin/env python3
'''
This script defines an asynchronous generator that yields random numbers
between 0 and 10 with a 1-second delay between each yield.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Asynchronous generator that yields random numbers with a delay.

    Yields:
        float: A random float between 0 and 10.

    Usage:
        async for num in async_generator():
            print(num)
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
