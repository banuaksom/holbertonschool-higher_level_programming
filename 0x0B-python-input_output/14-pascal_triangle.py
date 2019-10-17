#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle


def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
