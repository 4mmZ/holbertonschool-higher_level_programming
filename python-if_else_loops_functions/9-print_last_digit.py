#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        digit = number
        digit = digit * -1
        digit = digit % 10
    else:
        digit = number
        digit = digit % 10
    print("{}".format(digit), end='')
    return digit
