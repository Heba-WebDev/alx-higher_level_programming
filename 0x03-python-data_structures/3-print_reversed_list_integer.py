#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    reversed = my_list[::-1]
    for number in my_list:
        print("{:d}".format(number))
