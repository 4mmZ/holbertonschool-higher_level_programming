#!/usr/bin/python3
""" Doc """
import json


def load_from_json_file(filename):
    """ Func """
    with open(filename) as f:
        lines = json.load(f)
        return lines
