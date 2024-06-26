#!/usr/bin/python3
"""
State module for the models package
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """
    State class inherits from BaseModel and Base
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", back_populates="state")

    def __init__(self, *args, **kwargs):
        """
        Initialize State instance
        """
        super().__init__(*args, **kwargs)


Base.metadata.create_all(engine)

