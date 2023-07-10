#!/usr/bin/python3
"""Determins inhertance from a class"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class.
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    """

    return type(obj) == a_class
