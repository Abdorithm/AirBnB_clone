#!/usr/bin/pythonl
"""Test cases for the BaseModel
from /models/base_model.py

Unittest classes:
    TestBaseModel
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for testing instantiation of BaseModel."""

    def setUp(self):
        self.model = BaseModel()

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
        model_str = self.model.__str__()
        self.assertIn("[BaseModel] (2003)", model_str)
        self.assertIn("'id': '2003'", model_str)
        self.assertIn("'created_at': " + dt_repr, model_str)
        self.assertIn("'updated_at': " + dt_repr, model_str)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def tearDown(self):
        del self.model



if __name__ == '__main__':
    unittest.main()
