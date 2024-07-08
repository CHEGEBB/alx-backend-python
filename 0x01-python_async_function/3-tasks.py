#!/usr/bin/env python3
"""
asynchronous coroutine that takes an integer argument
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' 
    0-basic_async_syntax.wait_random coroutine wrapped into an asyncio.Task
    Implements task_wait_random function
    Args: max_delay: int
    Returns: asyncio.Task
    '''
    return asyncio.create_task(wait_random(max_delay))
