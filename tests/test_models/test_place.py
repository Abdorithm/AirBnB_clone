#!/usr/bin/python3
"""Test cases for the Place from models/place.py

Unittest classes:
    TestPlace
"""
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittest for testing the Place class."""

    def setUp(self):
        self.model = Place()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, Place)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.city_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.description, "")
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        self.assertEqual(self.model.latitude, 0.0)
        self.assertEqual(self.model.longitude, 0.0)
        self.assertEqual(self.model.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
