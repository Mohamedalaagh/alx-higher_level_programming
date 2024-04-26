#!/usr/bin/python3
"""Defines a module for appending text after a specified string in a file."""


def append_after(file_name="", search_string="", new_text=""):
    """Appends new_text after search_string in the file."""
    text = ""
    with open(file_name) as file_read:
        for line in file_read:
            text += line
            if search_string in line:
                text += new_text
    with open(file_name, "w") as file_write:
        file_write.write(text)
