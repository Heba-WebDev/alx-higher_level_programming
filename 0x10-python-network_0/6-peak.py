#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    newList = list_of_integers.sort(reverse=True)
    return newList[0]
