#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for count in range(0, len(my_list)):
        if count == idx:
            my_list.remove(count + 1)
            return my_list
