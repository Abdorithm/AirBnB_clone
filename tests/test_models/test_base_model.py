#!/usr/bin/python3
"""Test cases for the BaseModel from models/base_model.py

Unittest classes:
    TestBaseModel
"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for testing the BaseModel class."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        self.model = BaseModel()
        self.model_dict = self.model.to_dict()

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_instantiation(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_init(self):
        self.assertIsNotNone(self.model.id)
        self.assertIsNotNone(self.model.created_at)
        self.assertIsNotNone(self.model.updated_at)

    def test_save(self):
        updated_at = self.model.updated_at
        self.model.save()
        self.assertLess(updated_at, self.model.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        self.model.id = "2003"
        self.model.created_at = dt
        self.model.updated_at = dt
        model_str = str(self.model)
        self.assertIn("[BaseModel] (2003)", model_str)
        self.assertIn("'id': '2003'", model_str)
        self.assertIn("'created_at': " + dt_repr, model_str)
        self.assertIn("'updated_at': " + dt_repr, model_str)

    def test_to_dict(self):
        self.assertIsInstance(self.model_dict, dict)
        self.assertIn("id", self.model_dict)
        self.assertIn("created_at", self.model_dict)
        self.assertIn("updated_at", self.model_dict)
        self.assertIn("__class__", self.model_dict)
        self.assertEqual(self.model_dict['__class__'], 'BaseModel')

    def test_to_dict_added_attributes(self):
        self.model.name = "Abdo"
        self.model.phone = 420
        self.model_dict = self.model.to_dict()
        self.assertIn("name", self.model_dict)
        self.assertIn("phone", self.model_dict)

    def test_to_dict_datetime_attributes_are_str(self):
        self.assertEqual(str, type(self.model_dict["created_at"]))
        self.assertEqual(str, type(self.model_dict["updated_at"]))
        self.assertNotEqual(
            self.model.created_at, self.model_dict["created_at"]
        )
        self.assertNotEqual(
            self.model.updated_at, self.model_dict["updated_at"]
        )

    def test_date_attributes_are_datetime(self):
        self.assertEqual(datetime, type(self.model.created_at))
        self.assertEqual(datetime, type(self.model.updated_at))

    def test_init_with_kwargs(self):
        model2 = BaseModel(** self.model_dict)
        self.assertEqual(self.model.id, model2.id)
        self.assertEqual(self.model.created_at, model2.created_at)
        self.assertEqual(self.model.updated_at, model2.updated_at)
        self.assertNotEqual(self.model, model2)


if __name__ == '__main__':
    unittest.main()
