#!/usr/bin/python3

"""Class that inherts from list"""


class MyList(list):
    """Define MyList class"""


    def __init__(self, mylist):
        """Initialize constructor"""
        self.__mylist = mylist

    @property
    def mylist(self):
        """Get/set the list"""
        return self.__mylist
    @mylist.setter
    def mylist(self, value):
        self.__mylist = value

    def print_sorted(self):
        self.sort()
