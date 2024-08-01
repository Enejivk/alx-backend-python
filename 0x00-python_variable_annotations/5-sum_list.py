#!/usr/bin/env python3
"""return the total number of a"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculating the value in the list"""
    total = 0
    for value in input_list:
        total += value
    return total
