#!/usr/bin/python3
""" Doc """


def write_file(filename="", text=""):
    """ Func """
    with open(filename) as f:
        """ instance when the file is opened by the function"""
        lines = f.write(text)
        return lines
