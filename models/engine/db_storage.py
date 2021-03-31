#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json
import os
import sqlalchemy
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
classes = {"User": User,
           "Place": Place,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Review": Review}


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance of session and db_ojbect """
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),pool_pre_ping=True)
        self.reload()

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Returns dictionary result query of all models currently in storage"""
        query_results = []
        query_results.extend(self.__session.query(User).all())
        query_results.extend(self.__session.query(Place).all())
        query_results.extend(self.__session.query(State).all())
        query_results.extend(self.__session.query(City).all())
        query_results.extend(self.__session.query(Amenity).all())
        query_results.extend(self.__session.query(Review).all())
        new_dict = {}
        for obj in query_results:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict
            
        key = "{}.{}".
        return new_dict

    def close(self):
        """close current session"""
        self.__session.remove()


    def delete(self, ojb=None):
        """detele obj from the current session"""
        if obj:
            self.__session.delete(obj)

    def new(self, obj):
        """commits current state of session to the database"""
        if obj:
            self.__session.add()

    def save(self):
        """commits current instance to the database"""
        self.__session.commit()

    def reload(self):
        """  """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
