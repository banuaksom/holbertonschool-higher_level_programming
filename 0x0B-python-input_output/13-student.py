#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dict1 = {}
            for i in attrs:
                if i in self.__dict__:
                    dict1[i] = self.__dict__[i]
            return dict1
        return self.__dict__

    def reload_from_json(self, json):
        for i in self.__dict__:
            if i in json:
                self.__dict__[i] = json[i]
