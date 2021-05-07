#!/usr/bin/python3


def roman_to_int(roman_string):

    values = [1, 5, 10, 50, 100, 500, 1000]
    symbols = ["I", 'V', 'X', 'L', 'C', 'D', 'M']
    count = 0

    if roman_string:

        try:
            for i in range(len(roman_string)):

                for j in range(len(symbols)):
                    if roman_string[i] == symbols[j]:

                        try:
                            for x in range(len(symbols)):
                                if symbols[x] == roman_string[i + 1]:
                                    if x > j:
                                        count -= values[j]

                                    else:
                                        count += values[j]

                        except IndexError:
                            count += values[j]

            return count

        except TypeError:
            return 0

    return 0
