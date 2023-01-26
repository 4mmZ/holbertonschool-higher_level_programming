#!/usr/bin/python3


def uniq_add(my_list=[]):
    aux = [i for i in my_list if not i == my_list[i] ]
    return sum(aux) + 1
