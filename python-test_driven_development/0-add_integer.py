#!/usr/bin/python3
"""Module for add_integer function."""
import math


def add_integer(a, b=98):
    """Adds two integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
