#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """Initialize a new Square.
        """
        if size < 0:
            raise TypeError("size must be >= 0")
        elif not isinstance(size, int):
            raise ValueError("size must be an integer")
        self.__size = size
