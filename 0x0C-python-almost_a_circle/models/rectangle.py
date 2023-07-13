#!/usr/bin/python3
"""Class Rectangle"""
from .base import Base


class Rectangle(Base):
    """Initializes instance attributes
        Args:
            width (int): width of the ractangle
            height (int): height of rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrives value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of width"""
        self.__width = value

    @property
    def height(self):
        """Retrives value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height"""
        self.__height = value

    @property
    def x(self):
        """Retrives value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets value of x"""
        self.__x = value

    @property
    def y(self):
        """Retrives value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets value of y"""
        self.__y = value
