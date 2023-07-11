#!/usr/bin/python3

"""Class Student"""


class Student():
    """Define Student class"""
    def __init__(self, first_name, last_name, age):
        self.__firstname = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        return (self.__dict__)
