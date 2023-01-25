#!/usr/bin/env python3
"""Contains the function make_multiplier """

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns a function that multiplies a float by multiplier """
    def mult(num: float) -> float:
        """Multiplier retruned """
        return multiplier * num
    return mult
