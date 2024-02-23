#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = sorted([x for x in a_dictionary.values()])
    for key in a_dictionary.keys():
        if a_dictionary[key] == best[-1]:
            return key
