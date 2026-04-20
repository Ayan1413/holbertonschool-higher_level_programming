#!/usr/bin/python3
"""
Module for defining a Square class that inherits from Rectangle.

This module contains the `Square` class, which inherits from the `Rectangle` class.
It represents a square and includes methods to validate the size, calculate the area,
and provide a string representation of the square.

The `Square` class uses the `integer_validator` method inherited from `Rectangle` 
to validate the size of the square before assigning it to the private attribute.

Functions:
    Square: A class that represents a square, with methods to validate its size,
            compute its area, and provide a string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from the Rectangle class.

    This class inherits from the Rectangle class and validates that the size
    is a positive integer before assigning it to the private attribute. It also
    provides methods to calculate the area of the square (which is simply the
    area of a square) and return a string representation of the square.

    Attributes:
        __size (int): The size of the square, validated as a positive integer.

    Methods:
        __init__(self, size): Initializes a new Square object with size.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square in the format [Rectangle] <size>/<size>.
    """

    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.

        Validates the size using the integer_validator method from Rectangle.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        self.integer_validator("size", size)  # Validate size

        # Set the private attribute for size
        self.__size = size

        # Call the constructor of Rectangle to set width and height to the same size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        The area of the square is simply the size squared (size * size).

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        The string representation is in the format:
        [Rectangle] <size>/<size>

        Returns:
            str: The string representation in the format [Rectangle] <size>/<size>.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
