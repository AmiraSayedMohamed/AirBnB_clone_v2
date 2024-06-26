#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    __tablename__ = 'base_model'  # Optional: Specify a table name if using SQLAlchemy

    # Conditional column definitions based on storage type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True, unique=True)
        created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
        updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    else:
        id = ''
        created_at = datetime.utcnow()
        updated_at = datetime.utcnow()

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            if not hasattr(self, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(self, 'created_at'):
                setattr(self, 'created_at', datetime.utcnow())
            if not hasattr(self, 'updated_at'):
                setattr(self, 'updated_at', datetime.utcnow())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def delete(self):
        """Deletes this BaseModel instance from the storage"""
        from models import storage
        storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        res = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    res[key] = value.isoformat()
                else:
                    res[key] = value
        res['__class__'] = self.__class__.__name__
        return res

