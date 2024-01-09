#!/usr/bin/python3
"""
Defines a function for appending content to a UTF-8 encoded text file.

This function accepts a filename and text, appending the provided text to the end of the specified file.
It returns the number of characters successfully appended.

Args:
    filename (str): The name of the file to append to.
    text (str): The string to append to the file.

Returns:
    int: The number of characters appended to the file.
"""
def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

