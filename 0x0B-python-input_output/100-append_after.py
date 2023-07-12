#!/usr/bin/python3
"""Inserts a line of text to a file
after each line containing a specific string”"""


def append_after(filename="", search_string="", new_string=""):
    """OAppends string to a file"""
    with open(filename, 'r') as f:
        data = f.read()
        data = data.replace(search_string, new_string)
