#!/usr/bin/python3
"""
Defines a function for writing content to a UTF-8 encoded text file.

This function accepts a filename and text, writing the provided text to the specified file.
It returns the number of characters successfully written.

Args:
    filename (str): The name of the file to write.
    text (str): The text to be written to the file.

Returns:
    int: The number of characters written to the file.
"""
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

