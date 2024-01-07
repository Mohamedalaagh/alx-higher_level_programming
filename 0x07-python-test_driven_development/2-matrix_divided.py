#!/usr/bin/python3
"""Defines a matrix division function."""


def mat_divided(mat, d):
    """Divide all elements of a matrix.

    Args:
        mat (list): A list of lists of ints or floats.
        d (int/float): The divisor.
    Raises:
        TypeError: If the mat contains non-numbers.
        TypeError: If the mat contains rows of different sizes.
        TypeError: If d is not an int or float.
        ZeroDivisionError: If d is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(mat, list) or mat == [] or
            not all(isinstance(row, list) for row in mat) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in mat for num in row])):
        raise TypeError("mat must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(mat[0]) for row in mat):
        raise TypeError("Each row of the mat must have the same size")

    if not isinstance(d, int) and not isinstance(d, float):
        raise TypeError("d must be a number")

    if d == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / d, 2), row)) for row in mat])

