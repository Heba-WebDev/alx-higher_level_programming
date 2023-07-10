#!/usr/bin/python3
"""Object is an instance of a class that inherited from class"""


def inherits_from(obj, a_class):
    """Determines if an object is exactly an instance of a class.
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
