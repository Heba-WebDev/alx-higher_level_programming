#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = list()
    for i in range(0, len(my_list)):
        if(my_list[i] == 0):
            new_list.append(True)
        elif(my_list[i] == 1):
            new_list.append(False)
        elif(my_list[i] % 2 == 0):
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
