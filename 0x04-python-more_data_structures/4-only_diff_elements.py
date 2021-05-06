#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    new_list = []
    option = 0

    for i in set_1:
        for j in set_2:
            if i == j:
                option = 1
                break

        if option == 0:
            new_list.append(i)
        option = 0

    for i in set_2:
        for j in set_1:
            if i == j:
                option = 1
                break

        if option == 0:
            new_list.append(i)
        option = 0

    return new_list
