#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represents an amenity data set."""
    __tablename__ = 'amenities'

    # Conditional column definition based on storage type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    # Additional methods or properties can be added here if needed

    def to_dict(self):
        """Converts instance into dict format"""
        res = super().to_dict()
        return res

