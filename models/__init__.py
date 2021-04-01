#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or BDStorage
"""

from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":

    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
    print("INIT FILE DBstorage being used")
else:
    try:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.reload()
    except:
        print("file stroage not working")