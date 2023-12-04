#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if number < 0:
    x = -number
man = x % 10
if man > 5:
    print(f"Last digit of {number} is {man} and is greater than 5")
elif man == 0:
    print(f"Last digit of {number} is {man} and is 0")
else:
    print(f"Last digit of {number} is {man} and is less than 6 and not 0")
