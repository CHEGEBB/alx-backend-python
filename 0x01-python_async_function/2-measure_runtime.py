#!/usr/bin/env python3
'''2-measure_runtime.py file
'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Implements measure_time function
    Args: n: int, max_delay: int
    Body: Measure the total execution time for wait_n(n, max_delay)
    Returns: total_time / n -> float
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / n
