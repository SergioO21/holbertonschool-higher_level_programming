#!/usr/bin/python3
""" Rectangle Class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    # Declare a Rectangle based in ``BaseGeometry``.

    Args:

        width (int) = Rectangle width.
        height (int) = Rectangle height.
    """

    def __init__(self, width, height):
        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
