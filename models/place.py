#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review

try:
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))

except:
    print("place amenity did not work")


class Place(BaseModel, Base):
    """ A place to stay """
    try:
        __tablename__ = 'places'
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
        reviews = relationship("Review",
                               cascade="all, delete", backref="place")
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
        def amenities(self, obj):
            """Accepts only Amenity Objects"""
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
    except:
        print("setter not working")
