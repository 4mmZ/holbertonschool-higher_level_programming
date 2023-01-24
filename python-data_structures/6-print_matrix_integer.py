#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i in n:
            if matrix == 3:
                break
            print("{:d}".format(i), end=" ")
        print ("")
