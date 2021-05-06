#!/usr/bin/python3


def uniq_add(my_list=[]):

    j = my_list[0] - 1
    count = 0

    for i in my_list:
        if i > j:
            count += i

        j = i

    return count
