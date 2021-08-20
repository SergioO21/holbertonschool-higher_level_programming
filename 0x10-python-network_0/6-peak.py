#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    " Sort the list and return the last number. "

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
