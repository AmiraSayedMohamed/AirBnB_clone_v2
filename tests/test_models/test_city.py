#!/usr/bin/python3
"""Unittest module for the City class"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = City()
        self.assertIsInstance(instance, City)
        self.assertEqual(instance.name, '')
        self.assertEqual(instance.state_id, '')

if __name__ == "__main__":
    unittest.main()

