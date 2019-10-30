# -*- coding: utf-8 -*-
from flask_restful import Resource

from app.commands import *
from app.event_commands import EventCommands


class Event(Resource):
    def post(self):
        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return EventCommands(json_args).create_event()
