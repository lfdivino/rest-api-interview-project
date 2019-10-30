# -*- coding: utf-8 -*-

from api_888_interview.app.db_odds_commands import OddsCommandDB


class Odd(object):
    def __init__(self, json):
        self.json_event = json

    def update_odds_json_event(self, event):
        for selection in self.json_event['event']['markets'][0]['selections']:
            for event_selection in event['markets'][0]['selections']:
                if event_selection['id'] == selection['id']:
                    event_selection['odds'] = selection['odds']

        return event

    def update_odds(self):
        db_odds = OddsCommandDB()
        event = db_odds.select_event_by_id(self.json_event['event']['id'])
        if not event:
            return "The event id {} don't exists!".format(
                self.json_event['event']['id']), 400

        json_modified_odds = self.update_odds_json_event(event)

        result = db_odds.update_odds(event['id'], json_modified_odds)

        return True, 200
