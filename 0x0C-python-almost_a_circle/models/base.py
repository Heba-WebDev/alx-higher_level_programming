#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """Class initilization"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                result.append(dictionary)
        with open(filename, mode='w', encoding='UTF-8') as f:
            f.write(cls.to_json_string(result))
