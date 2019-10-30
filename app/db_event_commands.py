# -*- coding: utf-8 -*-

from app.db_connection import DatabaseConnection
from settings import *


class EventCommandsDB(object):
    def __init__(self):
        self.db = DatabaseConnection(MONGO_URI, MONGO_DATABASE, 'Events')

    def create_event(self, event):
        return self.db.db_collection.insert_one(event)

    def delete_event(self, event_id):
        return self.db.db_collection.delete_one({'id': event_id})

    def select_event_by_id(self, event_id):
        return self.db.db_collection.find_one({"id": event_id}, {"_id": 0})
