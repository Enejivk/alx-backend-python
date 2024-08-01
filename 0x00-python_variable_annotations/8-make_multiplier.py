#!/usr/bin/env python
"""Module that return function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This return a callable function"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
