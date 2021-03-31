#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("cities", backref="state", cascade="all, delete")

    def cities(self):
        """getter attr"""
        new_list = []
        for key, val in models.storage.all(City):
            if key.state_id == self.id:
                new_list[key] = value
        return new_list