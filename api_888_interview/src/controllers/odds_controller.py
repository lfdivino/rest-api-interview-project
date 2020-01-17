# -*- coding: utf-8 -*-

from .db_odds_controller import OddsCommandDB


class Odd(object):
    def __init__(self, json):
        self.json_event = json

    def update_odds_json_event(self, event):
        """Function responsible for updating the Odds in the ```Event```
        object and returning this modified event"""
        for selection in self.json_event['event']['markets'][0]['selections']:
            for event_selection in event['markets'][0]['selections']:
                if event_selection['id'] == selection['id']:
                    event_selection['odds'] = selection['odds']

        return event

    def update_odds(self):
        """Function responsible for validate if the ```Event```, them call
        the function to update the values and update the collection in the
        database"""
        db_odds = OddsCommandDB()
        event = db_odds.select_event_by_id(self.json_event['event']['id'])
        if not event:
            return "The event id {} don't exists!".format(
                self.json_event['event']['id']), 200

        json_modified_odds = self.update_odds_json_event(event)

        db_odds.update_odds(event['id'], json_modified_odds)

        return True, 200
