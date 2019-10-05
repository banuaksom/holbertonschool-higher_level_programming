#!/usr/bin/python3
def print_square(size):
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end='')
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
