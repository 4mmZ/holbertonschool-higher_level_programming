#!/usr/bin/python3
""" Doc """


def read_file(filename=""):
    with open(filename) as f:
        lines = f.read()
        print(lines)
