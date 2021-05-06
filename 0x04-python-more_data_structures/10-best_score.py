#!/usr/bin/python3


def best_score(a_dictionary):

    first = 0
    best_score = 0
    best_score_key = None

    if a_dictionary:
        for key, value in a_dictionary.items():
            if first == 0:
                best_score = value
                best_score_key = key
                first += 1

            if value > best_score:
                best_score = value
                best_score_key = key

    return best_score_key
