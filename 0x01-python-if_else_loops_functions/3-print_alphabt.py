#!/usr/bin/python3
first_ch, last_ch = ord("a"), ord("z")
for i in range(first_ch, last_ch - 1):
    if i == ord("e") or i == ord("q"):
        continue
    else:
        print("{}".format(chr(i)), end="")
