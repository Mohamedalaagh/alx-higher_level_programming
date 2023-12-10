#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = ()
    for i in range(2):
        if len(tuple_a) < (i+1):
            tuple_a += (0,)
        if len(tuple_b) < (i+1):
            tuple_b += (0,)
        tup += ((tuple_a[i]+ tuple_b[i]),)
    return tup
