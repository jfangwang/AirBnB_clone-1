#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
# from models.amenity import Amenity
metadata = Base.metadata

place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False,
                             primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False,
                             primary_key=True))


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

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
