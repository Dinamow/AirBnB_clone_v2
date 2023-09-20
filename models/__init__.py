#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import db_storage
import os

os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_TYPE_STORAGE'] = 'db'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = db_storage()
else:
    storage = FileStorage()
storage.reload()
