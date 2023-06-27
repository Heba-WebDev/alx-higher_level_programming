#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self._size = size
