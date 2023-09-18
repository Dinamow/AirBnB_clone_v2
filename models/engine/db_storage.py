#!/usr/bin/python3
"""this is class file"""
import os
from sqlalchemy import create_engine
from models.base_model import Base


class db_storage:
    """this is class"""
    __engine = None
    __session = None
    def __init__(self):
        usr = os.getenv("HBNB_MYSQL_USER")
        host = os.getenv("HBNB_MYSQL_HOST")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV", "none")
        ex = f"mysql+mysqldb://{usr}:{pwd}@{host}/{db}"
        self.__engine = create_engine(ex, pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        self.__session

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
