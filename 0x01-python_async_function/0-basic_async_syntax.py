#!/usr/bin/env python3

import asyncio

async def wait_random(max_delay=10):
    delaytime = random.uniform(1, max_delay)
    await asyncio.sleep(delaytime)
    return delaytime
