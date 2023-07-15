#!/usr/bin/python3
"""Class Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Initializes instance attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Iniltized a new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Defines the size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
