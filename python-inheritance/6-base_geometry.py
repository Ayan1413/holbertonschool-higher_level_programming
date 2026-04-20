#!/usr/bin/python3
"""
Module for BaseGeometry class.

This module contains the `BaseGeometry` class with a public instance method `area`
which raises an exception if called directly, to be implemented by subclasses.

Functions:
    BaseGeometry: A class that serves as a base for other geometry-related classes.
"""

class BaseGeometry:
    """
    A base class for geometry-related classes.

    This class serves as a base for other geometry-related classes. It contains
    an unimplemented method `area()`, which is expected to be overridden by
    subclasses to compute the area of specific geometric shapes.

    Methods:
        area(self): Raises an Exception indicating that this method must be
                    implemented by subclasses.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.

        This method should be overridden by subclasses to calculate the area
        of specific geometric shapes (e.g., rectangles, squares).
        
        Raises:
            Exception: Always raises an exception with the message 
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")
