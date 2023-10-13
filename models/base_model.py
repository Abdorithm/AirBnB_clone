#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
import cmd
from datetime import datetime
import models


class BaseModel(cmd.Cmd):
    """Represents BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initializes base class"""
        for key, val in kwargs.items():
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            if key == "created_at" or key == "updated_at":
                self.__dict__[key] = datetime.strptime(val, date_format)
            else:
                self.__dict__[key] = val
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """overriding the __str__ method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        cp_dict = self.__dict__.copy()
        cp_dict["created_at"] = self.created_at.isoformat()
        cp_dict["updated_at"] = self.updated_at.isoformat()
        cp_dict["__class__"] = self.__class__.__name__
        return cp_dict
