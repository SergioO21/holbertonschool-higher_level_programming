#!/usr/bin/python3
""" print_square function """


def print_square(size):
    """
    # This function prints a square with the character '#'

    Args:

        size (int) = The size length of the square

    - ``size`` must be an integer,
      otherwise raise a ``TypeError`` exception.

    - If ``size`` is less than (0),
      raise a ``ValueError`` exception.

    - If ``size`` is a float and is less than (0),
      raise a ``TypeError`` exception.
    """

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size != 0:

        for i in range(size):
            print("#" * size)
