#!/usr/bin/python3
"""
0x07. Python - Test-driven development
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    element_size = len(matrix[0])
    if isinstance(matrix, list):
        for element in matrix:
            if not isinstance(element, list):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            else:
                for i in element:
                    if not isinstance(i, (int, float)):
                        raise TypeError("matrix must be a matrix "
                                        "(list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for element in matrix:
        if len(element) != element_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    new_matrix = []
    for element in matrix:
        for element_1 in element:
            result.append(round(element_1 / div, 2))
        new_matrix.append(result)
        result = []
    return new_matrix
