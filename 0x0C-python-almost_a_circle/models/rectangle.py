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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

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

    def update(self, *args, **kwargs):
        """Updates attributes of an instance.

        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def area(self):
        """Method that returns the area of the rectangle object
        Args:
           Not arguments
        Return:
           Area of the rectangle object
        """
        return self.width * self.height

    def to_dictionary(self):
        """Returns the dictionary
        representation of a Rectangle"""
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
