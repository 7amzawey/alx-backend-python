#!/usr/bin/env python3
"""Take a str & an int or flaot and returns a tuple."""
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v * v))