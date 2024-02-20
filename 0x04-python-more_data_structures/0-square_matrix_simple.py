#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        new_mat.append([x**2 for x in i])
    return new_mat
