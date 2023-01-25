#!/usr/bin/env python3
"""Contains the function sum_mixed_list """
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """sums the items of a list of integers and floats """
    res: float = 0.0
    for i in mxd_lst:
        res += i
    return res
