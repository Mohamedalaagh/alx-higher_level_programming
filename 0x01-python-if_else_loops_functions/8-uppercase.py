#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{}".format(chr(ord("A") + (ord(str[i]) - ord("a")))) if  str[i] >= "a" and str[i] <= "z" else "{}".format(str[i]), end="")
    print()
