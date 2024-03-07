#!/usr/bin/python3
def safe_print_division(a, b):
    x = None
    try:
        x = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(x))
    return x
