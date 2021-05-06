#!/usr/bin/python3


def uniq_add(my_list=[]):

    second_list = my_list.copy()
    l_list = len(my_list)
    count = 0
    option = 0

    for i in range(l_list):
        for j in range(0, i):
            if my_list[i] == second_list[j]:
                option = 1
                break

        if option == 0:
            count += my_list[i]

        option = 0

    return count
