#!/usr/bin/python3
"""
doc
"""


def text_indentation(text):
    """
    doc
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    indent = True
    for spaces in text:
        if spaces in ".:?":
            print(spaces, end="\n\n")
            indent = True
        elif not indent or spaces != " ":
            print(spaces, end="")
            indent = False
