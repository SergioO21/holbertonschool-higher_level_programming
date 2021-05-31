#!/usr/bin/python3
""" File Reader """


def read_file(filename=""):
    """
    # Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (file) = Text file.
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")
