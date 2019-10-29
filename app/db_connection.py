# -*- coding: utf-8 -*-

from pymongo import MongoClient


class DatabaseConnection(object):
    def __init__(self, mongo_uri, mongo_database, nome_collection):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_database
        self.mongo_collection = nome_collection
        self.db_collection = self.create_connection_db()

    def connect_mongodb_cluster(self):
        client = MongoClient(self.mongo_uri)

        return client

    def connect_db(self, client_cluster):
        db = client_cluster[self.mongo_database]

        return db

    def connect_collection(self, db, nome_collection):
        collection = db[nome_collection]

        return collection

    def create_connection_db(self):
        client = self.connect_mongodb_cluster()
        client_db = self.connect_db(client)
        client_collection = self.connect_collection(
            client_db, self.mongo_collection
        )

        return client_collection
