#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class City(BaseModel):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'

    state_id = Column(String(60),  ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref="cities")
