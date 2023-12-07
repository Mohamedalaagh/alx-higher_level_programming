#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if "a" <= str[i] <= "z":
            k = chr(ord("A") + (ord(str[i]) - ord("a")))
        else:
            k = str[i]
        print(k, end="")
    print()
