#!/usr/bin/python3

""" Integers addition """


def add_integer(a, b=98):
    """Adds two numbers and returns the result as an integer.

        Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add. Defaults to 98.

        Returns:
        int: The sum of a and b, casted to an integer.

        Raises:
        TypeError: If either a or b is not an int or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
