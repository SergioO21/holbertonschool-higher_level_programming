#!/usr/bin/python3
""" JSON Encoder """

import json


def to_json_string(my_obj):
    """
    # Returns the JSON representation of an object (string).

    Args:

        my_obj (...) = Object to represent.
    """

    return json.dumps(my_obj)
