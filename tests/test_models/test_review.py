#!/usr/bin/python3
"""Test cases for the Review from models/review.py

Unittest classes:
    TestReview
"""
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittest for testing the Review class."""

    def setUp(self):
        self.model = Review()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, Review)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")


if __name__ == '__main__':
    unittest.main()
