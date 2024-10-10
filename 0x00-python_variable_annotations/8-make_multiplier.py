#!/usr/bin/env python3
"""Take a float multiplier as an argument and returns a function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """Take a float mulitpler and returns a function."""
    def multiply(x: float) -> float:
        """Multiply a number by x."""
        return (x * multiplier)
    return multiply
