#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx >= len(my_list):
        return
    else:
        print("Element at index {:d} is {}"
              .format(idx, element_at(my_list, idx)))
