#!/usr/bin/python3
"""Determins if object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Determines if an object is exactly an instance of a class.
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    """

    return isinstance(obj, a_class)
