#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    if os.getenv('HBNB_TYPE_STORAGE') ==

