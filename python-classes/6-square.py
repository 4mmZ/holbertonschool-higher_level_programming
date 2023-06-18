#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    class
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        aux = self.__position

        if len(aux) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(aux[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if int(aux[0]) < 0 or int(aux[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        iterator = self.__size
        my_tuple = self.__position
        j = 0
        i = 0
        if iterator == 0:
            print("\n", end="")
            return
        for b in range(my_tuple[1]):
            print()
        for i in range(iterator):
            for a in range(my_tuple[0]):
                print(" ", end="")
            for j in range(iterator - 1):
                print("#", end="")
            print("#")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        aux = self.__position
        if type(aux[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
