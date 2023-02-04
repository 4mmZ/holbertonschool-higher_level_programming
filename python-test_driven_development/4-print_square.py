#!/usr/bin/python3
"""
Doc
"""


def print_square(size):
    """
    Doc
    """
    square = size
    if type(square) is not int:
        raise TypeError("size must be an integer")
    if square < 0:
        raise ValueError("size must be >= 0")

    for high in range(square):
        for lenght in range(square):
            print("#", end="")
        print()
