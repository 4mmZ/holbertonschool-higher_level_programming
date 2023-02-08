#!/usr/bin/python3
"""
"""


class MyList(list):
    """
    """
    def print_sorted(self):
        aux = list.copy(self)
        sorted_aux = aux.sort()
        print(aux)