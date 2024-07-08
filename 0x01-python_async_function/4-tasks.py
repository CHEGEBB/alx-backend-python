#!/usr/bin/env python3
"""
asynchronous coroutine that takes an integer argument
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    This function
    Implements task_wait_n async routine
    Args: n -> int, max_delay -> int
    Body: spawn wait_random n times with the specified max_delay
    Return: list of all the delays (float values)
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
