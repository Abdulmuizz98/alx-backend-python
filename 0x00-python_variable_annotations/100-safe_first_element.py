#!/usr/bin/env python3
"""Contains the function safe_first_element """
from typing import Sequence, Any, Union
import types

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The types of the elements of the input are not known """
    if lst:
        return lst[0]
    else:
        return None
