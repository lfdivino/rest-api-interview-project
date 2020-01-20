# -*- coding: utf-8 -*-

from .db_connection import DBConnection
from ...settings import *


class DBEvent(DBConnection):
    """Class responsible to generate all the database functionalities
     involving the events in the Database

    :param db = A Stance from DatabaseConnection Class, set the connection to
    the collection ```Events```
     """
    def __init__(self):
        super(DBEvent, self).__init__(
            MONGO_URI, MONGO_DATABASE, 'Events')

    def create_event(self, event):
        """Return the result of the operation of inserting a new ```Event```
        in the collection
        """
        return self.db_collection.insert_one(event)

    def delete_event(self, event_id):
        """Return the result of the operation of deleting an ```Event```
        of the collection
        """
        return self.db_collection.delete_one({'id': event_id})

    def select_event_by_id(self, event_id):
        """Return the ```Event``` event with the informed id or return
        False"""
        return self.db_collection.find_one({"id": event_id}, {"_id": 0})
