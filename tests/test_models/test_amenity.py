#!/usr/bin/python3
"""Test cases for the Amenity from models/amenity.py

Unittest classes:
    TestAmenity
"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """Unittest for testing the Amenity class."""

    def setUp(self):
        self.model = Amenity()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, Amenity)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
