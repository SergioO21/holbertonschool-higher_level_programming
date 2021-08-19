#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):

    if len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]

    for number in list_of_integers[1:]:
        if number > peak:
            peak = number

    return peak
