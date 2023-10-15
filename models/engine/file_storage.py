#!/usr/bin/python3
"""This module defines a storage system for objects in a JSON file."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Define the storage class.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of objects in storage.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to storage.
        """
        self.__objects[
            "{}.{}".format(obj.__class__.__name__, obj.id)
            ] = obj

    def save(self):
        """
        Saves the storage dictionary to a JSON file.
        """
        with open(self.__file_path, "w") as f:
            json.dump(
                {
                    k: v.to_dict()
                    for k, v in self.__objects.items()
                },
                f
            )

    def reload(self):
        """
        Loads the storage dictionary from a JSON file.
        """
        try:
            with open(self.__file_path, "r") as f:
                objdicts = json.load(f)
                for val in objdicts.values():
                    self.new(eval(val["__class__"])(**val))
        except FileNotFoundError:
            pass
