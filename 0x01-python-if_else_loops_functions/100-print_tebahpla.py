#!/usr/bin/python3
x = 0
z = 0
for i in range(ord("a"), ord("z") + 1):
    print(chr(ord("a") + 25 - x) if z % 2 == 0 else chr(ord("A") + (ord("a") + 25 - x) - ord("a")), end="")
    x += 1
    z += 1
