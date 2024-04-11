#!/usr/bin/python3
"""Creating a class square """
class Square:
    " Calculate the square "
    def __init__(self, size=0):
        """ Creating a private attribute
        args:
            size(int): the size of the new square.
        """
        self.__size = size

