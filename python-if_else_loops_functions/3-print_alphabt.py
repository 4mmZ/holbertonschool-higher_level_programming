#!/usr/bin/python3
for var in range(97, 123):
    if var == 101 or var == 113:
        continue
    print("{}".format(chr(var)), end="")
