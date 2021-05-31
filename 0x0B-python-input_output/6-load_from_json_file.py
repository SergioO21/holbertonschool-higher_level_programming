#!/usr/bin/python3
""" Object Creator from a JSON file """

import json


def load_from_json_file(filename):
    """
    # Creates an Object from a “JSON file”.

    Args:
        filename (file) = Text file.

    Return: Object crated.
    """

    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.load(my_file)
