#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
