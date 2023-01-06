#!/usr/bin/env python3
"""Contains the function sum_list """
import typing

def sum_list(input_list: typing.List[float]) -> float:
    """Sums up two floats and returns """
    res: float = 0.0
    for i in input_list:
        res += i
    return res
