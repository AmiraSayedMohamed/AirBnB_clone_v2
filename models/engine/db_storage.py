#!/usr/bin/python3
"""Defines the DBStorage engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Represents a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects of a given class"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        
        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """Adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all tables from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

