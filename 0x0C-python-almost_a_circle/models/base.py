#!/usr/bin/python3

"""
Base module for Base class
"""

import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts to string"""
        s = "[]"
        if list_dictionaries is not None or list_dictionaries:
            return json.dumps(list_dictionaries)
        return s

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the list to file"""
        empty = []
        f = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                empty.append(i.to_dictionary())
        with open(f, mode='w', encoding='utf-8') as a_f:
            a_f.write(cls.to_json_string(empty))

    @staticmethod
    def from_json_string(json_string):
        """converts from string to list"""
        empty = []
        if json_string is not None or json_string:
            return json.loads(json_string)
        return empty

    @classmethod
    def create(cls, **dictionary):
        """creates the instances"""
        if cls.__name__ == "Square":
            r = cls(4)
        else:
            r = cls(4, 4)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """loads from file"""
        f = cls.__name__ + ".json"
        empty = []
        if f is not None or f:
            with open(f, encoding='utf-8') as a_f:
                new_list = cls.from_json_string(a_f.read())
            for i in new_list:
                empty.append(cls.create(**i))
        return empty
