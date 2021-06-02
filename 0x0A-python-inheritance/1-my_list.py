#!/usr/bin/python3
""" MyList Class """


class MyList(list):
    """
    # Inherits from list.

    - ``print_sorted(self)``: Prints the list, but sorted (ascending sort).
    """
    def print_sorted(self):
        print(sorted(self))
