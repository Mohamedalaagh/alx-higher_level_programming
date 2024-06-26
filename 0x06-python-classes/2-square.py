#!/usr/bin/python3
# 1-square by moalaa
"""Define a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Creating a private attribute with specific condition
    args:
        size(int): the size of the new square.
    Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
    """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
