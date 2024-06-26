#!/usr/bin/python3
"""Unit tests for the Place model."""
import os
from models.place import Place
from tests.test_models.test_base_model import TestBasemodel


class TestPlace(TestBasemodel):
    """Represents the tests for the Place model."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def _test_attribute_type(self, attribute_name, expected_type):
        """Tests the type of a given attribute."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            expected_type = type(None)
        self.assertEqual(type(getattr(new, attribute_name)), expected_type)

    def test_city_id(self):
        """Tests the type of city_id."""
        self._test_attribute_type('city_id', str)

    def test_user_id(self):
        """Tests the type of user_id."""
        self._test_attribute_type('user_id', str)

    def test_name(self):
        """Tests the type of name."""
        self._test_attribute_type('name', str)

    def test_description(self):
        """Tests the type of description."""
        self._test_attribute_type('description', str)

    def test_number_rooms(self):
        """Tests the type of number_rooms."""
        self._test_attribute_type('number_rooms', int)

    def test_number_bathrooms(self):
        """Tests the type of number_bathrooms."""
        self._test_attribute_type('number_bathrooms', int)

    def test_max_guest(self):
        """Tests the type of max_guest."""
        self._test_attribute_type('max_guest', int)

    def test_price_by_night(self):
        """Tests the type of price_by_night."""
        self._test_attribute_type('price_by_night', int)

    def test_latitude(self):
        """Tests the type of latitude."""
        self._test_attribute_type('latitude', float)

    def test_longitude(self):
        """Tests the type of longitude."""
        self._test_attribute_type('longitude', float)

    def test_amenity_ids(self):
        """Tests the type of amenity_ids."""
        self._test_attribute_type('amenity_ids', list)

