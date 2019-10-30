# -*- coding: utf-8 -*-
from flask_restful import Resource

from api_888_interview.app.commands import *
from api_888_interview.app.odds_commands import Odd


class Odds(Resource):
    """Class responsible for managing the update of the Event's Odds"""
    def post(self):
        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return Odd(json_args).update_odds()
