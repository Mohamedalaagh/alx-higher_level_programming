#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the hash character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size isn't an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for k in range(size):
        [print("#", end="") for l in range(size)]
        print("")
