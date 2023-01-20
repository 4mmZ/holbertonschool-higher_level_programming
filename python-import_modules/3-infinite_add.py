#!/usr/bin/python3

from sys import argv as args
total = 0
if __name__ == "__main__":
    for n in range(1, len(args)):
        total += int(args[n])
    print("{}".format(total))
