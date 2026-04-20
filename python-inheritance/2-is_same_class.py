#!/usr/bin/python3
""" 
Module for checking if an object is exactly an instance of a specified class.

This module contains a function `is_same_class` that checks if a given object
is exactly an instance of a specified class, and not an instance of a subclass.
It helps in confirming the type of an object in situations where exact type matching
is required.

Functions:
    is_same_class(obj, a_class): Returns True if obj is exactly an instance of a_class.
"""

def is_same_class(obj, a_class):
    """Tests if an object is exactly an instance of a specific class.

    Args:
        obj (any): object of any type.
        a_class (class): the class to compare the object with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return (type(obj) == a_class)
