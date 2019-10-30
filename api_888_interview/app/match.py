# -*- coding: utf-8 -*-
from flask_restful import Resource

from api_888_interview.app.commands import *
from api_888_interview.app.match_commands import MatchCommands


class MatchByID(Resource):
    """Class responsible for managing the routes of search matches by id"""
    def get(self, event_id=None):

        return MatchCommands(event_id=event_id).get_event_by_id()


class MatchByArgs(Resource):
    """Class responsible for managing the routes of search matches
    by parameters"""
    def get(self):
        """Function responsible to manage what parameter was passed via
        Querystring and call the correct function to return the matches"""
        parser = parser_get_arguments()
        args = parser.parse_args()

        if args.get('name'):
            return MatchCommands(name=args['name']).get_event_by_name()

        if args.get('sport'):
            return MatchCommands(sport=args['sport'],
                          ordering=args['ordering']).get_event_by_sport()

        return MatchCommands().get_events()
