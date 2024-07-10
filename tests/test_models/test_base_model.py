#!/usr/bin/python3
"""Unittest module for the BaseModel class"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_to_dict(self):
        """Test conversion of instance to dictionary"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_save(self):
        """Test if save method updates `updated_at`"""
        instance = BaseModel()
        prev_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(prev_updated_at, instance.updated_at)

if __name__ == "__main__":
    unittest.main()

