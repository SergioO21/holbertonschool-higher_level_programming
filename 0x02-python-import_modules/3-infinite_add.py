#!/usr/bin/python3

import sys


def run():
    argv = sys.argv
    addition = 0

    length = len(argv) - 1

    if length == 0:
        print("{}".format(addition))

    else:
        for args in argv:
            if args != "./3-infinite_add.py":
                addition += int(args)

    print("{}".format(addition))

if __name__ == "__main__":
    run()
