#!/usr/bin/env python3
"""Contains the function sum_list """


def sum_list(input_list: list[float]) -> float:
    """Sums up two floats and returns """
    res: float = 0.0
    for i in input_list:
        res += i
    return res
