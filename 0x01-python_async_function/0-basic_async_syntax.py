#!/usr/bin/env python3
"""Modules that return a random number"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that returns a random number after a delay"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
