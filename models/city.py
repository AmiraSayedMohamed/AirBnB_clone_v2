#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    
    # Conditional column definitions based on storage type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete, delete-orphan', backref='cities')
    else:
        name = ''
        state_id = ''
        
        @property
        def places(self):
            """Returns the places in this City"""
            from models import storage
            places_in_city = []
            for place in storage.all(Place).values():
                if place.city_id == self.id:
                    places_in_city.append(place)
            return places_in_city

