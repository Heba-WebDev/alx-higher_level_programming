#!/usr/bin/python3
"""Class Student"""


class Student():
    """Define Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dict representation of Student"""
        return self.__dict__
