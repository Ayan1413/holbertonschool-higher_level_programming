#!/usr/bin/python3
""" Python - Input/Output, task 5. To JSON string """
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (serialized string)

    Args:
        my_obj (any): object to be serialized
    """
    return json.dumps(my_obj)
