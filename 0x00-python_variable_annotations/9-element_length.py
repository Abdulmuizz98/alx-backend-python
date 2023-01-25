#!/usr/bin/env python3
"""Contains the function element_length """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Get the length of each of the iterables """
    return [(i, len(i)) for i in lst]
