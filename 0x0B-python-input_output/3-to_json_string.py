#!/usr/bin/python3
"""Defines a module for converting an object to JSON string"""

import json


def to_json_string(obj):
    """
    Returns the JSON representation of an object (as a string)
    """
    return json.dumps(obj)
