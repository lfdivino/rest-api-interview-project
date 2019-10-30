# -*- coding: utf-8 -*-

from api_888_interview.app.db_connection import DatabaseConnection
from api_888_interview.settings import *


class EventCommandsDB(object):
    """Class responsible to generate all the database functionalities
     involving the events in the Database

    :param db = A Stance from DatabaseConnection Class, set the connection to
    the collection ```Events```
     """
    def __init__(self):
        self.db = DatabaseConnection(MONGO_URI, MONGO_DATABASE, 'Events')

    def create_event(self, event):
        """Return the result of the operation of inserting a new ```Event```
        in the collection
        """
        return self.db.db_collection.insert_one(event)

    def delete_event(self, event_id):
        """Return the result of the operation of deleting an ```Event```
        of the collection
        """
        return self.db.db_collection.delete_one({'id': event_id})

    def select_event_by_id(self, event_id):
        """Return the ```Event``` event with the informed id or return
        False"""
        return self.db.db_collection.find_one({"id": event_id}, {"_id": 0})
