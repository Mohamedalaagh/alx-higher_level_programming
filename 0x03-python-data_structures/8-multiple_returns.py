#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    x = (len(sentence), )
    if not sentence:
        c = None
    else:
        c = (sentence[0], )
    tup = x + c
    return tup
