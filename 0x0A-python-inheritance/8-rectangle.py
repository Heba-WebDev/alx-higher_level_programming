#!/usr/bin/python3

"""Class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectabgle"""
    def __init__(self, width, height):
        """Constructor"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'width', width)
        self.__height = height
