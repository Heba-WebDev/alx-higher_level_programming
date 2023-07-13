#!/usr/bin/python3
"""Class Base"""


class Base:
    """Class initilization"""

    def __init__(self, id=None):
        """Instances of base"""
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
