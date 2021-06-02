#!/usr/bin/python3
""" Instance Identifier """


def is_same_class(obj, a_class):
    """
    # This function returns ``True`` if the object is exactly
      an instance of the specified class; otherwise ``False``.

    Args:

        obj (...) = Object.
        a_class = Class.
    """

    if type(obj) == a_class:
        return True

    return False
