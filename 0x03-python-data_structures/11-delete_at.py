#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    len_list = len(my_list)

    if idx >= 0 and idx < len_list:

        remove_value = my_list[idx]
        my_list.remove(remove_value)

    return my_list
