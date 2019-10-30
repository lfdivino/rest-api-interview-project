# -*- coding: utf-8 -*-

from app.db_event_commands import EventCommandsDB


class EventCommands(object):
    def __init__(self, json):
        self.json_event = json

    def create_event(self):
        db_event = EventCommandsDB()
        event = db_event.select_event_by_id(self.json_event['event']['id'])
        if event:
            return 'The event id {} already exists!'.format(event['id']), 400

        self.json_event["event"]["url"] = \
            "/api/v1/match/{}".format(self.json_event["event"]["id"])

        result = db_event.create_event(self.json_event["event"])

        return self.json_event['event']['id'], 200
