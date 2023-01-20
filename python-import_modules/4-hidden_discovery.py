#!/usr/bin/python3
import hidden_4


name = dir(hidden_4)
for n in name:
    if not n.startswith('__'):
        print("{}".format(n))
