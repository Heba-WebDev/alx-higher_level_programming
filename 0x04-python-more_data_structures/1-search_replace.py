#!/usr/bin/python3


def search_replace(my_list, search, replace):
    for item in my_list:
        if my_list[item] == search:
            my_list[item] = replace
