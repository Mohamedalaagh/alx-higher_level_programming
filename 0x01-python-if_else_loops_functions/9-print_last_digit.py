#!/usr/bin/python3
def print_last_digit(number):
    x = number
    if number < 0:
        x = -x
    x = x % 10
    print(x, end="")
    return x
