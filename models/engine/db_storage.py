#!/usr/bin/python3
"""This module defines the DBStorage class."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize instance of DBStorage."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        objects = {}
        session = self.__session()

        classes = [State, City, User, Place, Review, Amenity]

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = session.query(cls)
        else:
            query = session.query(State, City, User, Place, Review, Amenity)

        for obj in query:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """Add object to current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.remove()

