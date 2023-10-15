#!/usr/bin/python3
"""Test cases for the FileStorage from models/engine/file_storage

Unittest classes:
    TestFileStorage_instantiation
"""
import unittest
import json
import os
import models
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of the FileStorage class."""

    def test_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    
    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittest for testing methods of the FileStorage class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
    
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        obj = models.base_model.BaseModel()
        models.storage.new(obj)
        self.assertIn(
                "{}.{}".format(obj.__class__.__name__, obj.id),
                models.storage.all()
        )
 
    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(models.base_model.BaseModel(), None)

    def test_save(self):
        obj = models.base_model.BaseModel()
        models.storage.new(obj)
        models.storage.save()
        with open("file.json", "r") as f:
            obj_dict = json.load(f)
            self.assertIn(
                "{}.{}".format(obj.__class__.__name__, obj.id),
                obj_dict
            )

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)


    def test_reload(self):
        obj = models.base_model.BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertIn(
                "{}.{}".format(obj.__class__.__name__, obj.id),
                models.storage.all()
        )

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)
