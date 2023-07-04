#!/usr/bin/python3

""" Prints name """


def print_square(size):
    """Prints #.

        Args:
        size: int

        Returns:
        # that equals size

        Raises:
        TypeError: if size is not an int or is float and less than 0
        ValueError: if size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        print("#" * size)
