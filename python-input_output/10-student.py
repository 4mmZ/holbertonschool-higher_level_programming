#!/usr/bin/python3
""" Doc """


class Student:
    """ Class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        returned_list = {}
        if not attrs == None:
            for i in attrs:
                if hasattr(self, i):
                    returned_list[i] = getattr(self, i)
            return returned_list
        return self.__dict__
