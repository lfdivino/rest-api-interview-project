# -*- coding: utf-8 -*-

from .db_event_commands import EventCommandsDB


class Event(object):
    def __init__(self, json):
        self.json_event = json

    def create_event(self):
        db_event = EventCommandsDB()
        for event in db_event.select_event_by_id(self.json_event['id']):
            return 'The event id {} already exists!'.format(event['id']), 400

        result = db_event.create_event(self.json_event)

        return self.json_event['id'], 200
