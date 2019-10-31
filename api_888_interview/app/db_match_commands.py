# -*- coding: utf-8 -*-
import pymongo

from api_888_interview.app.db_event_commands import EventCommandsDB
from api_888_interview.settings import *


class MatchCommandsDB(EventCommandsDB):
    """Class responsible to control all the search of matches
    in the ```Events``` collection"""
    def select_events(self):
        """Return all the Events in the collection"""
        return self.db_collection.find({}, {'_id': 0})

    def select_event_by_name(self, event_name=None):
        """Return the event that have the specified name or return False"""
        return self.db_collection.find_one(
            {'name': event_name}, DB_FIELDS_RETURN
        )

    def select_event_by_sport(self, sport=None, ordering=None):
        """Return a list of all the event with the sport name, if ordering
        specified order the result by this field"""
        events = None

        if ordering:
            events = self.db_collection.find(
                {'sport.name': sport}, DB_FIELDS_RETURN
            ).sort([(ordering, pymongo.ASCENDING)])
        else:
            events = self.db_collection.find(
                {'sport.name': sport}, DB_FIELDS_RETURN
            )

        return events
