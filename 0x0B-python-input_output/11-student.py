#!/usr/bin/python3
"""
we declare a class and initialize some
instance atrributes
and then we crate a function that basically returns
the dictionary representation of the class
this is achieved by use of the __dict__ attribute of the object
"""


class Student:
    """
    a blueprint about a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves the dictionary representation
        of an instance of this class
        if attrs are provide it returns the dictionary of the attrs
        else
        return all of them
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict

    def reload_from_json(self, json):
        """
        this method is used to replace all attributes
        of the Student instance from this class
        the json id the dictionary we pass in to replace the
        instance with
        """
        for key in json:
            if key is 'first_name':
                self.first_name = json[key]
            elif key is 'last_name':
                self.last_name = json[key]
            else:
                self.age = json[key]
