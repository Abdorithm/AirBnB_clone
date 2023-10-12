#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
import cmd
from datetime import datetime


class BaseModel(cmd.Cmd):
    """Represents BaseModel class"""
    def __init__(self, id=None, created_at=None, updated_at=None):
        """initializes base class
            Args:
                id (int):
            Returns:
                None"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """overriding the __str__ method"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        self.__dict__["__class__"] = "BaseModel"
        for key in self.__dict__:
            if key == "updated_at":
                self.__dict__[key] = self.__dict__[key].isoformat()
            elif key == "created_at":
                self.__dict__[key] = self.__dict__[key].isoformat()
        return self.__dict__
