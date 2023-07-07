""" Integers Division """


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

        Args:
        matrix: a list of int or float
        div: an int or float to divide by

        Returns:
        int: The sum of a and b, casted to an integer.

        Raises:
        TypeError: If either a or b is not an int or float.
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not matrix or not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for i in rows:
            if type(i) is not int and type(i) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    list_len = len(matrix[0])
    for submatrix in matrix:
        if len(submatrix) != list_len:
            raise TypeError('Each row of the matrix must have the same size')

    new_list = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(round(n / div, 2))
        new_list.append(new_row)

    return new_list
