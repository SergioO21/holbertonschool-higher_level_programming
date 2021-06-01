#!/usr/bin/python3
""" Student Class """


class Student:
    """
    # Defines a student.

    Args:

        first_name (string) = First name.
        last_name (string) = Last name.
        age (int) = Age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
