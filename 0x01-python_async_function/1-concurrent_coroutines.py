#!/usr/bin/env python3
"""This return sorted list"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """This function return sorted list"""

    task = [wait_random(max_delay) for spawn_time in range(n)]
    res = await asyncio.gather(*task)

    for i in range(len(res)):
        for y in range(1, len(res)):
            if res[y-1] > res[y]:
                res[y-1], res[y] = res[y], res[y-1]
    return res
