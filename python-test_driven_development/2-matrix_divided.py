#!/usr/bin/python3
"""
Doc
"""


def matrix_divided(matrix, div):
    """
    Doc
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for count, value in enumerate(matrix):
        if len(matrix) > 0:
            if len(matrix[count - 1]) != len(matrix[count]):
                raise TypeError("Each row of the matrix \
must have the same size")
        for i in value:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    matrix_div = [[round(x / div, 2) for x in list] for list in matrix]
    return matrix_div
