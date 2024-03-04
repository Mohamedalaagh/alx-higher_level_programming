#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = None
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            j = i
        except IndexError:
            break
    print()
    return j + 1
