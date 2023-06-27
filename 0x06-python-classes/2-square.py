#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """Initialize a new Square.
        """
        try:
            self.__size = size
        except TypeError:
            print("ize must be an integer")
        except ValueError:
            print("size must be >= 0")
