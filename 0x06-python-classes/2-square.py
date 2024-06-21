#!/usr/bin/python3
"""Define a square"""


class Square:
    """Creating a private attribute with specific condition
    args:
        size(int): the size of the new square.
    """

    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
