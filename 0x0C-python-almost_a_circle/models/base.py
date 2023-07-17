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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file"""
        data = "[]"
        filename = cls.__name__ + ".json"
        if list_objs is not None and type(list_objs) is list:
            list_dict = []
            for obj in list_objs:
                if isinstance(obj, Base):
                    list_dict.append(obj.to_dictionary())
            data = cls.to_json_string(list_dict)
        with open(filename, encoding="utf-8", mode="w") as fp:
            fp.write(data)

    def from_json_string(json_string):
        """Returns he list of the JSON string
        representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all
        attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as f:
                obj_list = cls.from_json_string(f.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except Exception:
            return result
