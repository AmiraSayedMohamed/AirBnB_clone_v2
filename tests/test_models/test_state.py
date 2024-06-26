#!/usr/bin/python3
"""Unittest module for the State class"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = State()
        self.assertIsInstance(instance, State)
        self.assertEqual(instance.name, '')

if __name__ == "__main__":
    unittest.main()

