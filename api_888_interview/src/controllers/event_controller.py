# -*- coding: utf-8 -*-

from api_888_interview.src.database.db_event import DBEvent


class EventController:
    """Class responsible to treat the data from the NewEvent route and call
    the ```Events``` database functions
    :param: A JSON, JSON with the data from the NewEvent"""
    def __init__(self, json):
        self.json_event = json
        self.db_event = DBEvent()

    def create_event(self):
        """Function responsible to verify if the ```Èvent``` already exist,
        if False, call the Event database function to create a new on"""
        db_event = DBEvent()
        event = db_event.select_event_by_id(self.json_event['event']['id'])
        if event:
            return 'The event id {} already exists!'.format(
                self.json_event['event']['id']), 200

        self.json_event["event"]["url"] = \
            "/api/v1/match/{}".format(self.json_event["event"]["id"])

        db_event.create_event(self.json_event["event"])

        return self.json_event['event']['id'], 200
