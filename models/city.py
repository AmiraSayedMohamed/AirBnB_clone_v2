#!/usr/bin/python3
"""City Module for HBNB project"""

import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """The City class, contains state ID and name"""
    __tablename__ = 'cities'

    # Define attributes based on storage type
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    # Define relationships based on storage type
    places = relationship('Place', cascade='all, delete, delete-orphan', backref='cities') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None

