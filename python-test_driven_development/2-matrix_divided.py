#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor.
    Returns:
        A new matrix with elements divided by div.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # matrix-in list olduğunu yoxla
    if not isinstance(matrix, list) or matrix == [] or not matrix:
        raise TypeError(msg)

    # hər bir sətrin list olduğunu və içindəkilərin rəqəm olduğunu yoxla
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # sətir ölçülərinin eyniliyini yoxla
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div-in növünü yoxla
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # div-in 0 olmasını yoxla
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Hesablama və yuvarlaqlaşdırma
    return [[round(x / div, 2) for x in row] for row in matrix]
