#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="delete", backref="user")
    reviews = relationship("Review", cascade="delete", backref="user")
