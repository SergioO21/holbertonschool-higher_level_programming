#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:

    """ Defines a rectangle
    Args:
        width (int) = Rectangle width
        height (int) = Rectangle height
    """

    def __init__(self, width=0, height=0):

        self.height = height
        self.width = width

    @property
    def height(self):
        """ Retrieve the property value """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the property value """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """ Retrieve the property value """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the property value """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
