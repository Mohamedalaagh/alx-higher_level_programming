#!/usr/bin/python3
"""Defines a module for loading data from a JSON file"""

import json


def load_from_json_file(file_name):
    """Load data from a JSON file"""
    with open(file_name, encoding="utf-8") as file_loaded:
        return json.load(file_loaded)
