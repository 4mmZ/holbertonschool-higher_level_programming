#!/usr/bin/python3
""" Doc """
import json


def save_to_json_file(my_obj, filename):
    """ Func """
    with open(filename, 'w') as f:
        lines = f.write(json.dumps(my_obj))
        return lines
