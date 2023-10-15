#!/usr/bin/python3
"""Test cases for the User from models/user.py

Unittest classes:
    TestUser
"""
import unittest
from datetime import datetime
from models.user import User


class TestBaseModel(unittest.TestCase):
    """Unittest for testing the User class."""

    def setUp(self):
        self.model = User()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, User)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")


if __name__ == '__main__':
    unittest.main()
