#!/usr/bin/python3

"""Class Student"""


class Student:
    """Define Student class"""

    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
