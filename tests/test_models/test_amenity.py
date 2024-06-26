#!/usr/bin/python3
"""Unittest module for the Amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)
        self.assertEqual(instance.name, '')

if __name__ == "__main__":
    unittest.main()

