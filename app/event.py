# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource, reqparse
from .event_commands import Event

parser = reqparse.RequestParser()


class NewEvent(Resource):
    def post(self):
        json_args = request.get_json()

        if not json_args:
            return 'Invalid request json', 400

        return Event(json_args).create_event()
