#!/usr/bin/python3
""" Square Class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    # Defines a Square.

    Args:
        size (int) = Size of one side of the square.
    """

    def __init__(self, size):
        super().__init__(size, size)

        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
