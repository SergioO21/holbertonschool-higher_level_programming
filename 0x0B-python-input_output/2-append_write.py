#!/usr/bin/python3
""" File Writer """


def append_write(filename="", text=""):
    """
    # Appends a string at the end of a text file (UTF8).

    Args:

        filename (file) = Text file.
        text (string) = Text to add.

    Return: The number of characters added.
    """

    with open(filename, mode="a", encoding="utf-8") as my_file:
        my_file.write(text)

    return len(text)
