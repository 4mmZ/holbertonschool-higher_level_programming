#!/usr/bin/python3
"""
class Square
"""


class Square:
    """
    hola :D
    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integrer")
        if not (int(size) >= 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        area_aux = self.__size ** 2
        return area_aux
