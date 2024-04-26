#!/usr/bin/python3

"""Defines a module for converting a JSON string to an object"""

import json


def from_json_string(json_str):
    """
    Return a Python object from a JSON string
    """

    return json.loads(json_str)
