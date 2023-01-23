#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    for n in range(0, len(my_list)):
        if idx > n:
            return my_list
        elif n == idx:
            my_list[n] = element
            return my_list
