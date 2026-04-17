#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The string to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Flag to skip spaces at the start of a new line
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        print(char, end="")
        skip_space = False

        if char in ".?:":
            print("\n")
            skip_space = True
