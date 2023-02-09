#!/usr/bin/python3
""" Doc """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)
