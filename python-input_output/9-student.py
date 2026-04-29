#!/usr/bin/python3
"""Module to define a Student class."""

class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the public attributes of the student.
        """
        return vars(self)
