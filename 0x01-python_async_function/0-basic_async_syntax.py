#!/usr/bin/env python3
'''wait for random time and return the delay time'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''
    wait for random seconds and return the delay time
    '''
    delaytime = random.uniform(1, max_delay)
    await asyncio.sleep(delaytime)
    return delaytime
