#!/usr/bin/env python3
'''
This script imports an asynchronous generator from another module
and defines an asynchronous comprehension to collect its values.
'''
import asyncio
asyngen = __import__('0-async_generator').async_generator

async def async_comprehension():
    '''
    Asynchronous comprehension to collect values from an async generator.

    Returns:
        list: A list containing the values yielded by the async generator.

    Usage:
        result = await async_comprehension()
    '''
    return [i async for i in asyngen()]
