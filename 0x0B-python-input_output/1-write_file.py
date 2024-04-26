#!/usr/bin/python3
"""Defines a file writing module."""


def write_file(file_name="", content=""):
    """Writes a string to a UTF8 text file."""
    with open(file_name, "w", encoding="utf-8") as file:
        return file.write(content)
