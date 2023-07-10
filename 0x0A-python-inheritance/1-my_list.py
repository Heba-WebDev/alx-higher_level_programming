#!/usr/bin/python3

"""Class that inherts from list"""


class MyList(list):
    """Define MyList class"""
    def print_sorted(self):
        print(sorted(self))
