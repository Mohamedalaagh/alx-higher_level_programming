#!/usr/bin/python3
"""
has one function that multiply two integers
"""


def matrix_mul(m_a, m_b):
    """Function that return a multiplication of two matrices
    Args:
        m_a: Tha first matrix
        m_b: The second matrix
    Return:
        new matrices which is the result of multiplication of the two matrices
    Raises:
        TypeError: If either of arguments is not a list or a list of lists
        ValueError: If either of arguments is empty list or
            list contains empty list.
        TypeError: If any element in either of lists is not integer or float.
        TypeError: If either of arguments has unequal lists legnth.
        ValueError: If matrices cannot be multipulated mathematically.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a in [[], [[]]]:
        raise ValueError("m_a can't be empty")
    if m_b in [[], [[]]]:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if not all(type(i[j]) in [float, int] for j in range(len(i))):
            raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if not all(type(i[j]) in [float, int] for j in range(len(i))):
            raise TypeError("m_b should contain only integers or floats")

    for row in range(len(m_a) - 1):
        if len(m_a[row]) != len(m_a[row + 1]):
            raise TypeError("each row of m_a must be of the same size")
    for row in range(len(m_b) - 1):
        if len(m_b[row]) != len(m_b[row + 1]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for n in range(len(m_a[i])):
                element += m_a[i][n] * m_b[n][j]
            row.append(element)
        result_matrix.append(row)

    return result_matrix
