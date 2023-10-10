#!/usr/bin/env python3
import asyncio
asynccomp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    tasks = [asynccomp() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time
