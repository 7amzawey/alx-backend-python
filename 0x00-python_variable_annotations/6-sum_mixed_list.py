#!/usr/bin/env python3
"""Return the sum of a list of floats & ints."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list."""
    return sum(mxd_lst)
