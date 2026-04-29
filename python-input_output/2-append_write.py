#!/usr/bin/python3
"""
Module for appending a string to a text file and returning the number of characters added.

This module contains a function `append_write` that appends a string to the specified
file in UTF-8 encoding. If the file doesn't exist, it is created. The function returns
the number of characters added to the file.

Functions:
    append_write(filename="", text=""): Appends the string `text` to the file `filename`
                                         and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8) and returns the number of characters added.

    This function opens the specified file in append mode, which ensures that the string `text`
    is added to the end of the file without modifying its existing content. If the file doesn't exist,
    it is created. The function returns the number of characters added to the file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    
    Example:
        nb_characters_added = append_write("file.txt", "Hello again!")
        print(nb_characters_added)
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
