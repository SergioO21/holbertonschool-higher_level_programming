#!/usr/bin/python3
""" Square Class """


class Square:

    """ Defines a square
    Args:
        size (int) = Size of the square

    - If size is not an integer, raise a TypeError exception
      with the message: "size must be an integer"

    - If size is less than 0, raise a ValueError exception
      with the message: "size must be >= 0"
    """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """ Returns the current square area """

        return (self.__size ** 2)
