# -*- coding: utf-8 -*-
from flask_restful import Resource

from api_888_interview.src.utils.get_request_json import get_request_json
from api_888_interview.src.controllers.event_controller import EventController


class Event(Resource):
    """Class responsible for managing the routes of the NewEvents"""
    def post(self):
        """Function responsible to receive the POST request and start the
        Create Event functionality"""
        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return EventController(json_args).create_event()
