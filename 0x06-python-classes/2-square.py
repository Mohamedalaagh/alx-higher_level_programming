#!/usr/bin/python3
# 2-square.py
"""Square class definition"""


class Square:
    " Calculate the square "

    def __init__(self, size=0):
        """ Creating a private attribute
        args:
            size(int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
