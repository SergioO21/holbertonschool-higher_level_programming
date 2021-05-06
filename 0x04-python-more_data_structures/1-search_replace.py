#!/usr/bin/python3


def search_replace(my_list, search, replace):

    l_list = len(my_list)
    new_list = []

    for i in range(l_list):
        if my_list[i] == search:
            new_list.append(replace)

        else:
            new_list.append(my_list[i])

    return new_list
