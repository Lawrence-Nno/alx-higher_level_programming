#!/usr/bin/python3

"""A function that divides all elements of a matrix by a single integer/float"""


def matrix_divided(matrix, div):
    """ matrix must be a list of lists of integers or floats
    div must be an integer or float

    args:
        matrix of type matrix with equal columns
        div of type integer or float

    raises:
        TypeError: if a member isn't an integer or float
        TypeError: if all rows aren't equal
        TypeError: if div isn't an integer or a float
        ZeroDivisionError: if div is 0

    return:
        returns a matrix where all members are divided by div"""

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in lists] for lists in matrix]
