#!/usr/bin/python3
"""Unit tests for the City model."""
import os
from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestCity(TestBasemodel):
    """Represents the tests for the City model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def _test_attribute_type(self, attribute_name, expected_type):
        """Tests the type of a given attribute."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            expected_type = type(None)
        self.assertEqual(type(getattr(new, attribute_name)), expected_type)

    def test_state_id(self):
        """Tests the type of state_id."""
        self._test_attribute_type('state_id', str)

    def test_name(self):
        """Tests the type of name."""
        self._test_attribute_type('name', str)

