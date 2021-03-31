#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
metadata = Base.metadata

try:
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False)
                        )
except:
    print("place amenity did not work")

class Place(BaseModel):
    """ A place to stay """
    try:
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    except:
        print("place did not create")
    try:
        amenity_ids = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)
    except:
        print("amen id does not work")
    try:
        reviews = relationship("Review", cascade="delete", backref="place")
    except:
        print("revews does not work")
    # amenities = relationship("Amenity", secondary=place_amenity,
    #                          viewonly=False)
    try:
        @property
        def amenities(self):
            """Getter, may have to change this getter."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, item):
            """Accepts only Amenity Objects"""
            from models.amenity import Amenity
            if isinstance(item, Amenity):
                self.amenity_ids.append(item.id)
    except:
        print("setter not working")

