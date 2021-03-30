#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# will not need if array.extend(iterable) method for session query list
classes = {"BaseModel": BaseModel,
           "User": User,
           "Place": Place,
           'State': State,
           'City': City,
           'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance of session and db_ojbect """
        HBNB_MYSQL_USER = os.getenv['HBNB_MYSQL_USER']
        HBNB_MYSQL_PWD = os.getenv['']
        HBNB_MYSQL_HOST = os.getenv['']
        HBNB_MYSQL_DB = os.getenv['']
        HBNB_ENV = os.getenv['']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        for obj in array:
            key = "{}.{}".format(type(item).__name__, item.id)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        
                                                                           
    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def close(self):
        """  """


    def delete(self, ojb=None):

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        

    def reload(self):
        """  """
        
