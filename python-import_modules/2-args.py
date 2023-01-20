#!/usr/bin/python3

import sys

if __name__ == "__main__":
    for args in range(len(sys.argv)):
        count = int(args)
        if len(sys.argv) == 1:
            print("{} arguments.".format(len(sys.argv) - 1))
            break

        count = int(args)
        if count > 0:
            print('{}: {}'.format(count, sys.argv[args]))
            continue
        if len(sys.argv) < 3:
            print("{} argument:".format(len(sys.argv) - 1))
        elif len(sys.argv) > 2:
            print("{} arguments:".format(len(sys.argv) - 1))
