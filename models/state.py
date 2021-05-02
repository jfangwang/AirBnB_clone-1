#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """ State class """

    try:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

        @property
        def cities(self):
            """getter attr"""
            from models import storage
            new_list = []
            for key, value in storage.all(City).items():
                if value.to_dict()['state_id'] == self.id:
                    new_list.append(value)
            return new_list
    except:
        print("state did not work")
