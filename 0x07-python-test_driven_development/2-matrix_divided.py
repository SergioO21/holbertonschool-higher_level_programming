#!/usr/bin/python3
""" matrix_divided function """


def matrix_divided(matrix, div):
    """
    # Divides all elements of a matrix.

    Args:
        matrix (list) = The matrix
        div (int) = Matrix divisor

    - ``matrix`` must be a list of lists of integers or floats,
      otherwise raise a ``TypeError`` exception.

    - Each ``row of the matrix`` must be of the same size,
      otherwise raise a ``TypeError`` exception.

    - ``div`` must be a number (integer or float),
      otherwise raise a ``TypeError`` exception.

    - ``div`` can’t be equal to (0),
      otherwise raise a ``ZeroDivisionError`` exception.

    - All elements of the ``matrix`` should be divided by ``div``,
      rounded to 2 decimal places.

    Return: A new matrix.
    """

    different_size = "Each row of the matrix must have the same size"
    no_number = "matrix must be a matrix (list of lists) of integers/floats"
    rows_size = []
    new_matrix = []
    index_matrix = 0

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:

        rows_size.append(len(row))
        new_matrix.append([])

        for index in row:

            if type(index) != int and type(index) != float:
                raise TypeError(no_number)

            new_matrix[index_matrix].append(round((index / div), 2))

        index_matrix += 1

    for x in rows_size:
        if rows_size[0] != x:
            raise TypeError(different_size)

    return new_matrix
