#!/usr/bin/python3
"""Inserts a line of text to a file
after each line containing a specific string”"""


def append_after(filename="", search_string="", new_string=""):
    """Appends string"""
    with open(filename, 'r') as f:
        data = f.read()
    with open(filename, 'w') as f:
        for line in data:
            f.write(line)
            if (search_string in line):
                f.write(new_string + '\n')
