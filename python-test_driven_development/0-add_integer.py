#!/usr/bin/python3
"""Modul add_integer funksiyasını təqdim edir."""


def add_integer(a, b=98):
    """İki ədədi toplayır."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
