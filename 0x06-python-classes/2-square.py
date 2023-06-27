#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if size < 0:
            raise TypeError("size must be >= 0")
        elif not isinstance(size, int):
            raise ValueError("size must be an integer")
        self.__size = size
