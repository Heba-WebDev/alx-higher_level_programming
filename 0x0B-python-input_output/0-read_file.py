#!/usr/bin/python3
"""Reads a text file and prints it to stdout"""


def read_file(filename=""):
    """The file to print to stdout"""
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
