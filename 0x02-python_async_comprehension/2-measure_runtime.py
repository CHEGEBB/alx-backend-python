#!/usr/bin/env python3
'''2-measure_runtime.py file
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''This function will measure the runtime of async_comprehension
    four times and return the total runtime.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
