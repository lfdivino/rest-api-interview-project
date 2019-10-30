# -*- coding: utf-8 -*-
from flask_restful import Resource

from app.commands import *
from app.match_commands import MatchCommands


class MatchByID(Resource):
    def get(self, event_id=None):

        return MatchCommands(event_id=event_id).get_event_by_id()


class MatchByArgs(Resource):
    def get(self):
        parser = parser_get_arguments()
        args = parser.parse_args()

        if args.get('name'):
            return MatchCommands(name=args['name']).get_event_by_name()

        if args.get('sport'):
            return MatchCommands(sport=args['sport'],
                          ordering=args['ordering']).get_event_by_sport()

        return MatchCommands().get_events()
