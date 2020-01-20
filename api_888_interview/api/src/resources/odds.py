# -*- coding: utf-8 -*-
from flask_restful import Resource

from api.src.utils.get_request_json import get_request_json
from api.src.controllers.odds_controller import OddController


class Odds(Resource):
    """Class responsible for managing the update of the Event's Odds"""
    def post(self):
        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return OddController(json_args).update_odds()
