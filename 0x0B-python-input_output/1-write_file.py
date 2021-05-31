#!/usr/bin/python3
""" File Writer """


def write_file(filename="", text=""):
    """
    # Writes a string to a text file (UTF8).

    Args:

        filename (file) = Text file.
        text (string) = Text to write.

    Return: The number of characters written.
    """

    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(text)

    return len(text)
