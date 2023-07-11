#!/usr/bin/python3
"""Appends a string to the end of file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends to a file"""
    count = 0
    with open(filename, mode='a', encoding='UTF8') as f:
        count = f.write(text)
    return (count)
