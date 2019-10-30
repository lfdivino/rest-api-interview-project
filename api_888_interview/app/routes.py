# -*- coding: utf-8 -*-

from api_888_interview.app.event import Event
from api_888_interview.app.odds import Odds
from api_888_interview.app.match import MatchByID, MatchByArgs


def add_routes(api):
    api.add_resource(Event, '/api/v1/event')
    api.add_resource(MatchByID, '/api/v1/match/<event_id>')
    api.add_resource(MatchByArgs, '/api/v1/match/')
    api.add_resource(Odds, '/api/v1/odds')
