#!/usr/bin/python3
"""
This module defines a function lookup() that returns a list of attributes
and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to check for attributes and methods.

    Returns:
        list: A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
