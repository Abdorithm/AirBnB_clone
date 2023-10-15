#!/usr/bin/python3
"""Test cases for the State from models/state.py

Unittest classes:
    TestState
"""
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Unittest for testing the State class."""

    def setUp(self):
        self.model = State()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, State)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
