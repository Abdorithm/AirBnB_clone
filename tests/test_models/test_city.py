#!/usr/bin/python3
"""Test cases for the City from models/city.py

Unittest classes:
    TestCity
"""
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Unittest for testing the City class."""

    def setUp(self):
        self.model = City()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, City)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.state_id, "")
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
