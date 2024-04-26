#!/usr/bin/python3
"""Defines a module for generating Pascal's triangle."""


def pascal_triangle(rows):
    """Generate Pascal's triangle with the specified number of rows."""
    if rows <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != rows:
        current_row = triangle[-1]
        new_row = [1]
        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
