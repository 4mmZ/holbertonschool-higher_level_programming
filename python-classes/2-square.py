#!/usr/bin/python3

"""
class Square again
"""


class Square:
    """
    comment
    """
    def __init__(self, __size=0):
        if (type(__size) is not int):
            raise TypeError("size must be an integer")

        if not (int(__size) >= 0):
            raise ValueError("size must be >= 0")
        self.__size = __size
