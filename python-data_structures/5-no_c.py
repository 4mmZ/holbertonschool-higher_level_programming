#!/usr/bin/python3


def no_c(my_string):
    string = my_string.translate({ord('c'): None})
    string = string.translate({ord('C'): None})
    return string
