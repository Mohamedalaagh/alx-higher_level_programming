#!/usr/bin/python3

"""Defines a module for saving an object to a JSON file"""

import json


def save_to_json_file(obj, file_name):
    """
    Writes an object to a JSON file.
    """

    with open(file_name, mode='w', encoding='utf-8') as file:
        json.dump(obj, file, ensure_ascii=False)
