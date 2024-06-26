#!/usr/bin/python3
"""Unittest module for the Place class"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = Place()
        self.assertIsInstance(instance, Place)
        self.assertEqual(instance.city_id, '')
        self.assertEqual(instance.user_id, '')
        self.assertEqual(instance.name, '')
        self.assertEqual(instance.description, '')
        self.assertEqual(instance.number_rooms, 0)
        self.assertEqual(instance.number_bathrooms, 0)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.price_by_night, 0)
        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 0.0)

if __name__ == "__main__":
    unittest.main()

