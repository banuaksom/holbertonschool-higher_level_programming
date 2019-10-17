#!/usr/bin/python3
import math


def factorial(i, j):
    return math.factorial(i) // (math.factorial(j) * math.factorial(i - j))


def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i, j))
        triangle.append(row)
    return triangle
