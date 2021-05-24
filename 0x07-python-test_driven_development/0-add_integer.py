#!/usr/bin/python3
""" add_integer function """


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:

        a (int, float) = First Value
        b (int, float) = Second Value


    - If 'a' or 'b' are floats,
      they must be converted to integers.

    Return: The addition of a and b (int)
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)

    if type(b) == float:
        b = int(b)

    return (a + b)
