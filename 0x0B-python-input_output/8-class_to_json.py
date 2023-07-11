#!/usr/bin/python3
"""Returns the dictionary description with
simple data structure for JSON serialization
of an object"""


def class_to_json(obj):
    """Class to JSON"""
    return obj.__dict__
