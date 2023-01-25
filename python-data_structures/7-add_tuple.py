#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_b) < 2:
        tuple_aux = list(tuple_b)
        tuple_aux.append(0)
        aux = tuple(tuple_aux)
        result1 = add_tuple(tuple_a, aux)
        return result1
    while len(tuple_a) < 2:
        tuple_aux2 = list(tuple_a)
        tuple_aux2.append(0)
        aux2 = tuple(tuple_aux2)
        result2 = add_tuple(aux2, tuple_b)
        return result2
    if len(tuple_b) > 2 and len(tuple_a) > 2:
        apl = list(tuple_b)
        cp = list(tuple_a)
        apl = tuple(apl[:2])
        cp = tuple(cp[:2])
        recu = add_tuple(apl, cp)
        return recu
    result = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return result
