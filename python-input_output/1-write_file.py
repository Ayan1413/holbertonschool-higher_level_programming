#!/usr/bin/python3
"""
Module for writing a string to a text file and returning the number of characters written.

This module contains a function `write_file` that writes a string to a specified file
in UTF-8 encoding. If the file doesn't exist, it is created. If the file already exists,
its content is overwritten.

Functions:
    write_file(filename="", text=""): Writes the string `text` to the file `filename`
                                       and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns the number of characters written.

    This function opens the specified file in write mode (which overwrites the content
    if the file already exists). The string `text` is written to the file in UTF-8 encoding.
    
    Args:
        filename (str): The name of the file to be written to.
        text (str): The text to be written into the file.

    Returns:
        int: The number of characters written to the file.
    
    Example:
        nb_characters = write_file("myfile.txt", "Hello, World!")
        print(nb_characters)
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
