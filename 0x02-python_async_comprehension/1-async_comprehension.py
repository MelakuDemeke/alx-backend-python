#!/usr/bin/env python3
import asyncio
asyngen = __import__('0-async_generator').async_generator

async def async_comprehension():
    return [i async for i in asyngen()]
