#!/usr/bin/env python3
"""Module that return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creating a turple"""
    return (k, float(v ** 2))
