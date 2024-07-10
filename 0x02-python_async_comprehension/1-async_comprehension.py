#!/usr/bin/env python3
"""
This module contains the function for task 1 of the project
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function will collect 10 random numbers using an async generator
    and return them in a list
    """
    result = [i async for i in async_generator()]
    return result
