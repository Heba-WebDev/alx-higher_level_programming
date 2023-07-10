#!/usr/bin/python3
"""
This program use the inherit for create a new Rectangle
"""


prevRectangle = __import__('9-rectangle').Rectangle


class Square(prevRectangle):
    """
    Class Square inherits from Rectangle class
    """

    def __init__(self, size):
        """Constructor of new Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """This method return the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """This method return the representation of the Square"""
        return '[Square] {:d}/{:d}'.format(self.__width, self.__height)
