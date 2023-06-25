#!/usr/bin/python3
"""
doc
"""


class MyList(list):
    """
    doc
    """
    def print_sorted(self):
        aux = list.copy(self)
        sorted_aux = aux.sort()
        print(aux)
