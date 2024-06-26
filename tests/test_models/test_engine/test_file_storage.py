#!/usr/bin/python3
"""Unittest module for the FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'file', "FileStorage tests skipped if not using file storage")
class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Tear down test environment"""
        del self.storage

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test that new adds an object to the storage"""
        initial_count = len(self.storage.all())
        new_instance = BaseModel()
        self.storage.new(new_instance)
        self.storage.save()
        self.assertGreater(len(self.storage.all()), initial_count)

    def test_save(self):
        """Test that save properly saves objects to the file"""
        new_instance = BaseModel()
        self.storage.new(new_instance)
        self.storage.save()
        key = f"BaseModel.{new_instance.id}"
        self.assertIn(key, self.storage.all())

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
        new_instance = BaseModel()
        self.storage.new(new_instance)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{new_instance.id}"
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()

