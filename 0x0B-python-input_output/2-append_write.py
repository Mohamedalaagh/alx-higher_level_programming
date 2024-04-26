#!/usr/bin/python3
"""Defines a module for appending a string to a file."""


def append_write(file_name="", content=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(file_name, "a", encoding="utf-8") as file:
        return file.write(content)
