# -*- coding: utf-8 -*-
import pymongo

from app.db_event_commands import EventCommandsDB
from settings import *


class MatchCommandsDB(EventCommandsDB):
    def select_events(self):
        return self.db.db_collection.find({}, {'_id': 0})

    def select_event_by_name(self, event_name=None):
        return self.db.db_collection.find_one(
            {'name': event_name}, DB_FIELDS_RETURN
        )

    def select_event_by_sport(self, sport=None, ordering=None):
        events = None

        if ordering:
            events = self.db.db_collection.find(
                {'sport.name': sport}, DB_FIELDS_RETURN
            ).sort([(ordering, pymongo.ASCENDING)])
        else:
            events = self.db.db_collection.find(
                {'sport.name': sport}, DB_FIELDS_RETURN
            )

        return events
