#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
