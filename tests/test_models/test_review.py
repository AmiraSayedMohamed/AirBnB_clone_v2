#!/usr/bin/python3
"""Unittest module for the Review class"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = Review()
        self.assertIsInstance(instance, Review)
        self.assertEqual(instance.place_id, '')
        self.assertEqual(instance.user_id, '')
        self.assertEqual(instance.text, '')

if __name__ == "__main__":
    unittest.main()

