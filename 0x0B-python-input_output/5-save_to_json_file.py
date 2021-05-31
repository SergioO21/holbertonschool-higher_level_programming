#!/usr/bin/python3
""" JSON Writer """

import json


def save_to_json_file(my_obj, filename):
    """
    # Writes an Object to a text file, using a JSON representation.

    Args:

        my_obj (...) = Object to represent.
        filename (file) = Text file.
    """

    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
