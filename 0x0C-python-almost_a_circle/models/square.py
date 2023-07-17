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

    def update(self, *args, **kwargs):
        """Updates the Rectangle"""
        if args is not None:
            attributes = ['id', 'size', 'x', 'y']

            for i, arg in enumerate(args):
                if i > len(attributes):
                    break
                setattr(self, attributes[i], arg)

        if (args is None or len(args) == 0) and kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary
        representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
