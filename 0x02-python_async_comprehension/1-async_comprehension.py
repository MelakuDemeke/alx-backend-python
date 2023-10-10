#!/usr/bin/env python3
import asyncio
asyngen = __import__('1-async_comprehension').async_generator

async def async_comprehension():
    return [i async for i in asyngen()]
