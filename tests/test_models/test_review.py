#!/usr/bin/python3
"""Unit tests for the Review model."""
import os
from models.review import Review
from tests.test_models.test_base_model import TestBasemodel


class TestReview(TestBasemodel):
    """Represents the tests for the Review model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def _test_attribute_type(self, attribute_name):
        """Tests the type of a given attribute."""
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(getattr(new, attribute_name)), expected_type)

    def test_place_id(self):
        """Tests the type of place_id."""
        self._test_attribute_type('place_id')

    def test_user_id(self):
        """Tests the type of user_id."""
        self._test_attribute_type('user_id')

    def test_text(self):
        """Tests the type of text."""
        self._test_attribute_type('text')

