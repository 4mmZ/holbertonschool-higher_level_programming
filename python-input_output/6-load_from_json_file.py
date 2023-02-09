#!/usr/bin/python3
""" Doc """
import json


def load_from_json_file(filename):
    """ Func """
    open_json = json.dumps(filename)
    with open(open_json) as f:
        lines = json.load(f)
        return lines
