# -*- coding: utf-8 -*-

from app.db_match_commands import MatchCommandsDB


class MatchCommands(object):
    def __init__(self, event_id=None, name=None, sport=None, ordering=None):
        self.event_id = event_id
        self.name = name
        self.sport = sport.capitalize() if sport else sport
        self.ordering = ordering

    def get_events(self):
        db_match = MatchCommandsDB()
        event = [event for event in db_match.select_events()]

        return self.verify_event_db_return(event)

    def get_event_by_id(self):
        db_match = MatchCommandsDB()
        event = db_match.select_event_by_id(int(self.event_id))

        return self.verify_event_db_return(event)

    def get_event_by_name(self):
        db_match = MatchCommandsDB()
        event = db_match.select_event_by_name(self.name)

        return self.verify_event_db_return(event)

    def get_event_by_sport(self):
        db_match = MatchCommandsDB()
        events = [event for event in db_match.select_event_by_sport(
            self.sport, self.ordering)]

        return self.verify_event_db_return(events)

    def verify_event_db_return(self, event):
        if not event:
            return 'Match not found!', 404

        return event, 200

