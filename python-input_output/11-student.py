#!/usr/bin/python3
"""Module for Student class with serialization and deserialization."""


class Student:
    """A class to represent a student with first_name, last_name, age."""

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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If `attrs` is provided, only include those attributes.
        Otherwise, return all attributes.

        Args:
            attrs (list of str): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the instance.
        """
        if attrs is None:
            return vars(self)
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        """
        Replaces all attributes with the data in the dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
