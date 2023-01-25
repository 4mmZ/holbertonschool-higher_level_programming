#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_b) < 2:
        tuple_aux = list(tuple_b)
        tuple_aux.append(0)
        aux = tuple(tuple_aux)
        result1 = add_tuple(tuple_a, aux)
        return result1
    result = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return result
