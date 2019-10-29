# -*- coding: utf-8 -*-

from .db_connection import DatabaseConnection
from settings import *


class EventCommandsDB(object):
    def __init__(self):
        self.db = DatabaseConnection(MONGO_URI, MONGO_DATABASE, 'Events')

    def select_event_by_id(self, event_id=None):
        if not event_id:
            return False

        return self.db.db_collection.find({'id': event_id})

    def select_event_by_name(self, event_name=None):
        if not event_name:
            return False

        return self.db.db_collection.find('/{}/'.format(event_name))

    def create_event(self, event):
        return self.db.db_collection.insert_one(event)

    def delete_event(self, event_id):
        return self.db.db_collection.delete_one({'id': event_id})
