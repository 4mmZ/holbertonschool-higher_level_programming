#!/usr/bin/python3
"""
a and b must be integers or floats,
otherwise raise a TypeError exception with
the message a must be an integer or b must be an integer

"""


def add_integer(a, b=98):
    """
    def integer
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
