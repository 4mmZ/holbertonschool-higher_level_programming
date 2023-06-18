#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    class
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        iterator = self.__size
        j = 0
        i = 0
        if iterator == 0:
            print("\n", end="")
            return
        for i in range(iterator):
            for j in range(iterator - 1):
                print("#", end="")
            print("#")
