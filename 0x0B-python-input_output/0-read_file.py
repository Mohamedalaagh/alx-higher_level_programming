#!/usr/bin/python3
"""
Defines a function to vividly showcase the contents of a UTF-8 encoded text file on the standard output.
"""

def display_file_content(filename=""):
    """
    Open and read a UTF-8 encoded text file, presenting its vibrant contents on the standard output.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

