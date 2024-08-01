#!/usr/bin/env python3
from typing import List, Union
"""Module that add mixed List"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Adding mixed List"""
    total:float = 0.0
    for value in mxd_lst:
        total += value
    return total
