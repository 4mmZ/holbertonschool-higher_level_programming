#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i,j in enumerate(n):
            print("{:d}".format(j), end="")
            if i < len(n) -1:
                print(" ", end='')
        print("")
