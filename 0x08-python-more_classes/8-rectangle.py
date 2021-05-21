#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:

    """ Defines a rectangle
    Args:
        width (int) = Rectangle width
        height (int) = Rectangle height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def area(self):
        """ Returns the current rectangle area """

        return self.__width * self.__height

    def perimeter(self):
        """ Returns the current rectangle perimeter """

        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns the rectangle with the character '#' """

        rectangle = ""

        if self.__width != 0 and self.__height != 0:

            for i in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width

                if i != self.__height - 1:
                    rectangle += "\n"

        return rectangle

    def __repr__(self):
        """ Returns the representation of the rectangle """

        width = str(self.__width)
        height = str(self.__height)

        return "Rectangle(" + width + ", " + height + ")"

    def __del__(self):
        """ Print a message when a Rectangle instance is deleted """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2

        return rect_1
