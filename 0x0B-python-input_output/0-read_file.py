#!/usr/bin/python3
"""Defines a file reading module."""


def read_file(file_name=""):
    """
    read_file function
    Reads a text file (UTF8) and prints its contents to standard output
    """
    with open(file_name, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
