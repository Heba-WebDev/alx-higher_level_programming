#!/usr/bin/python3

"""List of available attributes and methods of an object"""

def lookup(obj):
    """The object to return its attributes and methods"""

    return list(dir(obj))
