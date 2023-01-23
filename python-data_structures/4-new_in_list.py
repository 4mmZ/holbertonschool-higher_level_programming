#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    if idx < 0:
        return my_list
    for n in range(len(my_list)):
        if n == idx:
            my_new_list[n] = element
            return my_new_list
    if idx > n:
        return my_list
