#!/usr/bin/python3

change = 0

for i in range(90, 64, -1):

    if change == 0:
        i = i + 32
        change = 1

    else:
        change = 0

    print("{}".format(chr(i)), end="")
