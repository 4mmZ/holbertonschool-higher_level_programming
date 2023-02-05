#!/usr/bin/python3
"""
    Class Rectangle
"""


class Rectangle:
    """
        Empty class
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        aux = self.__width
        if type(aux) is not int:
            raise TypeError("width must be an integer")
        if aux < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        aux = self.__width
        if type(aux) is not int:
            raise TypeError("width must be an integer")
        if aux < 0:
            raise ValueError("width must be >= 0")
