#!/usr/bin/python3
""" Doc """


def read_file(filename=""):
    """ Func """
    with open(filename) as f:
        """ instance when the file is opened by the function"""
        lines = f.read()
        print(lines)
