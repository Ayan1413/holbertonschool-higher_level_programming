#!/usr/bin/python3
"""
Module for defining a Rectangle class that inherits from BaseGeometry.

This module contains the `Rectangle` class, which inherits from `BaseGeometry`.
It includes methods to validate the rectangle's dimensions, calculate its area,
and provide a string representation of the rectangle in the format [Rectangle] <width>/<height>.

The `Rectangle` class validates that the `width` and `height` are positive integers
using the inherited `integer_validator` method from `BaseGeometry`.

Functions:
    Rectangle: A class representing a rectangle, with methods to validate dimensions, 
               calculate the area, and provide a string representation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    This class represents a rectangle, with methods to validate its dimensions 
    and compute its area. It inherits from the BaseGeometry class to ensure 
    that only valid dimensions are assigned to the rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes the rectangle with given width and height.
        area(self): Computes the area of the rectangle.
        __str__(self): Returns the string representation of the rectangle in the format
                        [Rectangle] <width>/<height>.
    """

    def __init__(self, width, height):
        """Initializes the Rectangle with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates the input using integer_validator to ensure width and height are 
        positive integers.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle in the format
                 [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
