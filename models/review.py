#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    try:
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    except:
        print("place id does not work")
    try:
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    except:
        print("user id does not work")
