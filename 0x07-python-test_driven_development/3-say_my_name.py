#!/usr/bin/python3

""" Prints name """


def say_my_name(first_name, last_name=""):
    """Prints name.

        Args:
        first_name: string
        last_name: string

        Returns:
        string: The full name

        Raises:
        TypeError: If either first_name or last_name are not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
