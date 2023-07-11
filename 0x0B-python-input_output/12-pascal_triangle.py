#!/usr/bin/python3
"""Returns a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n"""
    my_list = []
    if n <= 0:
        return my_list

    for i in range(n):
        if i == 0:
            my_list.append([1])
        else:
            new_list = [0] * (i+1)
            for j in range(len(new_list)):
                if j == 0 or j == len(new_list) - 1:
                    new_list[j] = 1
                else:
                    new_list[j] = my_list[i-1][j-1] + my_list[i-1][j]
            my_list.append(new_list)

    return my_list
