import os

from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()


def init_app(app: Flask):
	mongo.init_app(app, uri=f"mongodb://{os.environ['MONGO_INITDB_ROOT_USERNAME']}:{os.environ['MONGO_INITDB_ROOT_PASSWORD']}@localhost:27017/{os.environ['MONGO_INITDB_DATABASE']}?authSource=admin")
