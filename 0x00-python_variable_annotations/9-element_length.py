#!/usr/bin/env python3
"""Return a list"""
from typing import Iterable, Tuple, Sequence, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of lengths of a number"""
    return [(i, len(i)) for i in lst]
