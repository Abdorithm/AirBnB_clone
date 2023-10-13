#!/usr/bin/python3
"""This module defines a storage system for objects in a JSON file."""
import json
from models.base_model import BaseModel


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to storage.
        """
        FileStorage.__objects[
            "{}.{}".format(obj.__class__.__name__, obj.id)
            ] = obj

    def save(self):
        """
        Saves the storage dictionary to a JSON file.
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {
                    k: v.to_dict()
                    for k, v in FileStorage.__objects.items()
                },
                f
            )

    def reload(self):
        """
        Loads the storage dictionary from a JSON file.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                objdicts = json.load(f)
                for val in objdicts.values():
                    self.new(eval(val["__class__"])(**val))
        except FileNotFoundError:
            pass
