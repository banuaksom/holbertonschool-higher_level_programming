#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    else:
        for i in matrix:
            if any(type(j) != int and type(j) != float for j in i) \
                    or type(matrix) != list or len(i) == 0:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        matrix_length = len(matrix[0])
        for i in matrix:
            if matrix_length != len(i):
                raise TypeError("Each row of the matrix must have \
the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i] for i in matrix]
