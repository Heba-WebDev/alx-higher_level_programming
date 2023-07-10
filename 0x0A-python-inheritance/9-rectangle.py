#!/usr/bin/python3
"""
This program use the inherit for create Rectangle
"""


originalRectangle = __import__('8-rectangle').Rectangle


class Rectangle(originalRectangle):
    """
    Class Rectangle based in BaseGeometry
    """

    def __init__(self, width, height):
        """Constructor of Retangle"""
        originalRectangle.integer_validator(self, 'width', width)
        self.__width = width
        originalRectangle.integer_validator(self, 'height', height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the representation of the Rectangle"""
        return print("[Rectangle] {}/{}".format(self.__width, self.__height))
