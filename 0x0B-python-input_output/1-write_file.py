#!/usr/bin/python3
"""Writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes to a file"""
    count = 0
    with open(filename, mode='w', encoding='UTF8') as f:
        count = f.write(text)
    return (count)
