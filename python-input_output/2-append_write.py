#!/usr/bin/python3
""" Doc """


def append_write(filename="", text=""):
    """ Func """
    with open(filename, 'a') as f:
        """ instance when the file is opened by the function"""
        lines = f.write(text)
        return lines
