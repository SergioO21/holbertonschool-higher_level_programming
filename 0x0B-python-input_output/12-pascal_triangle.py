#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """
    # Returns a list of lists of integers representing the Pascal’s triangle.

    Args:

        n (int) = Number of rows.
    """

    pascal_triangle = [[1]]
    row = [1]

    if n <= 0:
        return ([])

    for i in range(1, n):

        if len(row) < 2:
            row.append(1)
            pascal_triangle.append(row)

        else:

            len_row = len(row)
            row2 = []
            row2.append(1)

            for x in range(len(row)):

                if (x + 1) < len(row):
                    row2.append(row[x] + row[x + 1])

            row2.append(1)
            row = row2
            pascal_triangle.append(row2)

    return (pascal_triangle)
