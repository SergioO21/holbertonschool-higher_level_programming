#!/usr/bin/python3
""" Base Class """

import json


class Base:
    """
    # Defines the Base class of the project

    Args:
        id (int) = Object id.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of ``list_dictionaries`` """

        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """

        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation to a file """

        json_name = cls.__name__ + ".json"
        json_rep = []

        if list_objs is not None:

            for obj in list_objs:
                json_rep.append(cls.to_dictionary(obj))

        with open(json_name, mode="w", encoding="utf-8") as json_file:
            json_file.write(cls.to_json_string(json_rep))

    @classmethod
    def create(cls, **dictionary):
        """ Create a dummy instance and apply its real values """

        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances based on a JSON file """

        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_file = f.read()

        except FileNotFoundError:
            return instances

        objs = cls.from_json_string(json_file)

        for obj in objs:
            instances.append(cls.create(**obj))

        return instances
