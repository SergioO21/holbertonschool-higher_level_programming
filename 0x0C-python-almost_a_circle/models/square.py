#!/usr/bin/python3
""" Square Class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    # Defines a Square based on Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):

        self.size = size

        super().__init__(self.__size, self.__size, x, y, id)

    def __str__(self):
        st = "[Square] ({:d}) {:d}/{:d}".format(self.id, self.x, self.y)
        st += " - {:d}".format(self.width)
        return st

    def to_dictionary(self):

        r_dict = {"id": self.id, "size": self.__size, "x": self.x, "y": self.y}
        return r_dict

    def update(self, *args, **kwargs):

        if not args or len(args) == 0:
            for key, value in kwargs.items():

                if key == "id":
                    self.id = value
                elif key == "size":
                    self.__size = self.width = self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
            return

        for i in range(len(args)):

            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.__size = self.width = self.height = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]
            else:
                break

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")

        self.width = self.height = self.__size = value
