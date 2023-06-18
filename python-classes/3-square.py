#!/usr/bin/python3
"""
class square
"""


class Square:
    """
    class square
    """
    def __init__(self, __size=0):
        self.__size = __size

    def area(self):
        area_aux = int(self.__size) ** 2
        return area_aux
