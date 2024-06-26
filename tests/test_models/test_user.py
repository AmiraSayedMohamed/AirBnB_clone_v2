#!/usr/bin/python3
"""Unittest module for the User class"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = User()
        self.assertIsInstance(instance, User)
        self.assertEqual(instance.email, '')
        self.assertEqual(instance.password, '')
        self.assertEqual(instance.first_name, '')
        self.assertEqual(instance.last_name, '')

if __name__ == "__main__":
    unittest.main()

