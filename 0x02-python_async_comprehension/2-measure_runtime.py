#!/usr/bin/env python3
'''
This script measures the total execution time of running the
async_comprehension() function concurrently four times.
'''
import asyncio
asynccomp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the total execution time of running async_comprehension()
    4 times concurrently.
    
    Returns:
    float: The total execution time in seconds.
    '''
    start_time = time.time()
    tasks = [asynccomp() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time
