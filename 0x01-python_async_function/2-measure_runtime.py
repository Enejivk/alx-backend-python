#!/usr/bin/env python3
"""module that measure the execution time of async code"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """getting the exact time it take to get the complete function"""

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    estimated_time = stop_time - start_time
    return estimated_time/n
