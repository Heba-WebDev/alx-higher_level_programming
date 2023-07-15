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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrives value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrives value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrives value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        

    def display(self):
        """Prints in stdout the Rectangle
        instance with the character #"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()
