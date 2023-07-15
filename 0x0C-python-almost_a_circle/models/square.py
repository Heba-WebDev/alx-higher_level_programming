#!/usr/bin/python3
"""Class Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Initializes instance attributes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Iniltized a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
