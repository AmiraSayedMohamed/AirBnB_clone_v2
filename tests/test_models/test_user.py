#!/usr/bin/python3
"""Unit tests for the User model."""
import os
from models.user import User
from tests.test_models.test_base_model import TestBasemodel


class TestUser(TestBasemodel):
    """Represents the tests for the User model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def _test_attribute_type(self, attribute_name):
        """Tests the type of a given attribute."""
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(getattr(new, attribute_name)), expected_type)

    def test_first_name(self):
        """Tests the type of first_name."""
        self._test_attribute_type('first_name')

    def test_last_name(self):
        """Tests the type of last_name."""
        self._test_attribute_type('last_name')

    def test_email(self):
        """Tests the type of email."""
        self._test_attribute_type('email')

    def test_password(self):
        """Tests the type of password."""
        self._test_attribute_type('password')

