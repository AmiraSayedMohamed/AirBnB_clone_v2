#!/usr/bin/python3
"""Unit tests for the Amenity model."""
import os
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBasemodel


class TestAmenity(TestBasemodel):
    """Represents the tests for the Amenity model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def _test_attribute_type(self, attribute_name):
        """Tests the type of a given attribute."""
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(getattr(new, attribute_name)), expected_type)

    def test_name(self):
        """Tests the type of name."""
        self._test_attribute_type('name')

