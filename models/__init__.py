#!/usr/bin/python3
"""Create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

classes_dict = {
            'BaseModel': BaseModel,
            'User': User
        }
storage = FileStorage()
storage.reload()
