#!/usr/bin/python3

from sys import argv


def run():

    if len(argv) - 1 == 0:
        print("{} argmuments.".format(len(argv) - 1))

    else:
        print("{} argmuments:".format(len(argv) - 1))

        for i in range(1, len(argv)):
                print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    run()
