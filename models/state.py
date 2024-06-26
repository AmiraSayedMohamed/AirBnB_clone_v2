#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    # Conditional column definition based on storage type
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    # Conditional property or relationship definition based on storage type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state

