#!/usr/bin/python3
"""
Module for creating a Square class that inherits from Rectangle.

This module contains a `Square` class which inherits from `Rectangle`. The `Square`
class has specific behavior for the square's size and its area calculation, while
still utilizing the `integer_validator` method for validating the size. The class
also overrides the `__str__` method to print the description of the square.

Functions:
    Square: A class that represents a square, inheriting from Rectangle.
"""

class BaseGeometry:
    """
    Base class for geometric shapes with basic validation functionality.
    """
    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle, validated as a positive integer.
        __height (int): The height of the rectangle, validated as a positive integer.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle object with width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle in the format [Rectangle] <width>/<height>.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle object."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.

    This class inherits from `Rectangle` and overrides methods to adapt them 
    for squares. It ensures that the width and height of the square are 
    equal and validates the size as a positive integer.

    Attributes:
        __size (int): The size of the square, validated as a positive integer.

    Methods:
        __init__(self, size): Initializes a new Square object with size.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square in the format [Square] <size>/<size>.
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
        [Square] <size>/<size>

        Returns:
            str: The string representation in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
#!/usr/bin/python3
"""
Module for creating a Square class that inherits from Rectangle.

This module contains a `Square` class which inherits from `Rectangle`. The `Square`
class has specific behavior for the square's size and its area calculation, while
still utilizing the `integer_validator` method for validating the size. The class
also overrides the `__str__` method to print the description of the square.

Functions:
    Square: A class that represents a square, inheriting from Rectangle.
"""

class BaseGeometry:
    """
    Base class for geometric shapes with basic validation functionality.
    """
    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle, validated as a positive integer.
        __height (int): The height of the rectangle, validated as a positive integer.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle object with width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle in the format [Rectangle] <width>/<height>.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle object."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.

    This class inherits from `Rectangle` and overrides methods to adapt them 
    for squares. It ensures that the width and height of the square are 
    equal and validates the size as a positive integer.

    Attributes:
        __size (int): The size of the square, validated as a positive integer.

    Methods:
        __init__(self, size): Initializes a new Square object with size.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square in the format [Square] <size>/<size>.
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
        [Square] <size>/<size>

        Returns:
            str: The string representation in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
