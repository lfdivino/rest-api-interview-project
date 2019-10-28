# -*- coding: utf-8 -*-


class Event(object):
    def __init__(self, json):
        self.json_event = json

    def create_event(self):
        return self.json_event['id'], 200
