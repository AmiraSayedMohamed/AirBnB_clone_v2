#!/usr/bin/python3
"""
BaseModel module for the models package
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage

Base = declarative_base()


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """
        Save instance to database
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """
        Delete instance from database
        """
        storage.delete(self)

    def to_dict(self):
        """
        Return dictionary representation of instance
        """
        new_dict = dict(self.__dict__)
        new_dict.pop("_sa_instance_state", None)
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict

    def __str__(self):
        """
        Return string representation of instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        Return string representation of instance
        """
        return self.__str__()

Base.metadata.create_all(engine)

