#!/usr/bin/python3

import sys

argv = sys.argv

length = len(argv) - 1
i = 1

if length == 0:
    print("{} argmuments.".format(length))

else:
    print("{} argmuments:".format(length))

    for args in argv:

        if args != "./2-args.py":
            print("{}: {}".format(i, args))
            i += 1
