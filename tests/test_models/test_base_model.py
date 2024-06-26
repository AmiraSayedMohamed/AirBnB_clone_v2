#!/usr/bin/python3
"""Unit tests for the BaseModel."""
import os
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel, Base


class TestBasemodel(unittest.TestCase):
    """Represents the tests for the BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Performs setup operations before each test."""
        pass

    def tearDown(self):
        """Performs cleanup operations after each test."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests the initialization of the model class."""
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """Tests the default instantiation."""
        instance = self.value()
        self.assertEqual(type(instance), self.value)

    def test_kwargs(self):
        """Tests instantiation with kwargs."""
        instance = self.value()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        """Tests instantiation with kwargs containing an int."""
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_save(self):
        """Tests the save method."""
        instance = self.value()
        instance.save()
        key = self.name + "." + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str(self):
        """Tests the __str__ method."""
        instance = self.value()
        self.assertEqual(str(instance), '[{}] ({}) {}'.format(self.name, instance.id, instance.__dict__))

    def test_to_dict(self):
        """Tests the to_dict method."""
        instance = self.value()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict, instance.to_dict())
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

        instance.firstname = 'Celestine'
        instance.lastname = 'Akpanoko'
        self.assertIn('firstname', instance.to_dict())
        self.assertIn('lastname', instance.to_dict())

        new_instance = self.value(id='012345', created_at=datetime.today().isoformat(), updated_at=datetime.today().isoformat())
        self.assertEqual(new_instance.to_dict()['id'], '012345')

        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(self.value(id='u-b34', age=13).to_dict()['age'], 13)
            self.assertEqual(self.value(id='u-b34', age=None).to_dict()['age'], None)

        self.assertIn('__class__', instance.to_dict())
        self.assertNotIn('__class__', instance.__dict__)
        self.assertNotEqual(instance.to_dict(), instance.__dict__)
        self.assertNotEqual(instance.to_dict()['__class__'], instance.__class__)

        with self.assertRaises(TypeError):
            self.value().to_dict(None)
        with self.assertRaises(TypeError):
            self.value().to_dict(self.value())
        with self.assertRaises(TypeError):
            self.value().to_dict(45)
        self.assertNotIn('_sa_instance_state', instance_dict)

    def test_kwargs_none(self):
        """Tests instantiation with None as kwargs."""
        kwargs = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.value(**kwargs)

    def test_kwargs_one(self):
        """Tests instantiation with a single key-value pair."""
        kwargs = {'Name': 'test'}
        new_instance = self.value(**kwargs)
        self.assertTrue(hasattr(new_instance, 'Name'))

    def test_id(self):
        """Tests the type of id."""
        instance = self.value()
        self.assertEqual(type(instance.id), str)

    def test_created_at(self):
        """Tests the type of created_at."""
        instance = self.value()
        self.assertEqual(type(instance.created_at), datetime)

    def test_updated_at(self):
        """Tests the type of updated_at."""
        instance = self.value()
        self.assertEqual(type(instance.updated_at), datetime)
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_delete(self):
        """Tests the delete method."""
        from models import storage
        instance = self.value()
        instance.save()
        self.assertIn(instance, storage.all().values())
        instance.delete()
        self.assertNotIn(instance, storage.all().values())

