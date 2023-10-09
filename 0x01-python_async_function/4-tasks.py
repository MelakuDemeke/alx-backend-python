#!/usr/bin/env python3
'''
wait for random time and return the delay time in list
'''
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
tak_3 = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawn wait_random n times with the specified max_delay.
    Return the list of all the delays (float values) in ascending order.
    '''
    tasks = [tak_3(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
