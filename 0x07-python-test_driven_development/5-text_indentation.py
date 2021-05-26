#!/usr/bin/python3
""" text_indentation function """


def text_indentation(text):
    """
    # This function prints a text with 2 new lines
      after each of these characters: '.', '?' and ':'.

    Args:

        text (str) = The text.

    - ``text`` must be a string,
      otherwise raise a ``TypeError`` exception.
    """

    initial = final = printed = 0

    if type(text) != str:
        raise TypeError("text must be a string")

    while initial < len(text):
        if text[initial] != " ":
            break

        initial += 1

    final = initial

    for final in range(len(text)):

        printed = 0

        if text[final] == '.' or text[final] == '?' or text[final] == ':':

            final += 1
            print(text[initial:final])
            print()

            while final < len(text):

                if text[final] != " ":
                    break
                final += 1

            initial = final
            printed = 1

    if printed == 0:
        print(text[initial:(final + 1)], end="")
