# -*- coding: utf-8 -*-

from api_888_interview.app.db_event_commands import EventCommandsDB


class EventCommands(object):
    """Class responsible to treat the data from the NewEvent route and call
    the ```Events``` database functions
    :param: A JSON, JSON with the data from the NewEvent"""
    def __init__(self, json):
        self.json_event = json

    def create_event(self):
        """Function responsible to verify if the ```Èvent``` already exist,
        if False, call the Event database function to create a new on"""
        db_event = EventCommandsDB()
        event = db_event.select_event_by_id(self.json_event['event']['id'])
        if event:
            return 'The event id {} already exists!'.format(event['id']), 400

        self.json_event["event"]["url"] = \
            "/api/v1/match/{}".format(self.json_event["event"]["id"])

        result = db_event.create_event(self.json_event["event"])

        return self.json_event['event']['id'], 200
