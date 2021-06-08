#!/usr/bin/python3
""" Rectangle Class """

from models.base import Base


class Rectangle(Base):
    """
    # Defines a Rectangle.

    Args:

        width (int) = Rectangle width.
        height (int) = Rectangle height.
        x (int) = X coordinate.
        y (int) = Y coordinate.
        id (int, None) = Rectangle id.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):

        st = "[Rectangle] ({:d}) {:d}/{:d}".format(self.id, self.__x, self.__y)
        st += " - {:d}/{:d}".format(self.__width, self.__height)
        return st

    def to_dictionary(self):
        """ Returns the dictionary representation of a ``Rectangle`` """

        r_dict = {"id": self.id, "width": self.__width}
        r_dict_2 = {"height": self.__height, "x": self.__x, "y": self.__y}
        r_dict.update(r_dict_2)

        return r_dict

    def area(self):
        """ Returns the area value of the ``Rectangle`` instance """

        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the ``Rectangle`` instance with the character '#'
        """

        for y in range(self.__y):
            print()

        for x in range(self.__height):
            if self.__x != 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """

        if not args or len(args) == 0:
            for key, value in kwargs.items():

                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
            return

        for i in range(len(args)):

            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]
            else:
                break

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
