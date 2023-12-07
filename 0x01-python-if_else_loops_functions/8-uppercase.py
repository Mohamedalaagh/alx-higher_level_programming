#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i] >= "a" and str[i] <= "z":
            print("{}".format(chr(ord("A") + (ord(str[i]) - ord("a")))), end="")
        else:
            print("{}".format(str[i]), end="")
    print()
