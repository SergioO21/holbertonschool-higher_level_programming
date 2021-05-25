#!/usr/bin/python3
""" say_my_name function """


def say_my_name(first_name, last_name=""):
    """
    # This function prints: My name is <first name> <last name>

    Args:

        first_name (str) = First name
        last_name (str) = Last name

    - ``first_name`` and ``last_name`` must be strings otherwise,
      raise a ``TypeError`` exception.
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
