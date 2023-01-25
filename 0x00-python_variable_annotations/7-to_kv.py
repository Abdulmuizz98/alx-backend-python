#!/usr/bin/env python3
"""Contains the function to_kv """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns the string k and the square of v """
    return (k, v**2)
