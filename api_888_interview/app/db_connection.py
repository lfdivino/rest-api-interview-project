# -*- coding: utf-8 -*-

from pymongo import MongoClient
import ssl


class DatabaseConnection(object):
    """Class responsible for creating the connections to the
    Mongodb Cloud Cluster, the Database itself and to the collection

    :param mongo_uri = A String, the URL to the Mongodb Cluster
    :param mongo_database = A String, The Database name
    :param mongo_collection = A String, The Collection name
    :param db_collection = A Function, responsible for the connection itself
    """
    def __init__(self, mongo_uri, mongo_database, nome_collection):
        self.mongo_uri = mongo_uri
        self.mongo_database = mongo_database
        self.mongo_collection = nome_collection
        self.db_collection = self.create_connection_db()

    def connect_mongodb_cluster(self):
        """Function responsible for the connection to the Mongodb
        Cloud Cluster"""
        client = MongoClient(
            self.mongo_uri, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

        return client

    def connect_db(self, client_cluster):
        """Function responsible for selecting the database inside the Cluster"""
        db = client_cluster[self.mongo_database]

        return db

    def connect_collection(self, db, nome_collection):
        """Function responsible for selecting the collection inside the DB"""
        collection = db[nome_collection]

        return collection

    def create_connection_db(self):
        """Function responsible for establish the full connection"""
        client = self.connect_mongodb_cluster()
        client_db = self.connect_db(client)
        client_collection = self.connect_collection(
            client_db, self.mongo_collection
        )

        return client_collection
