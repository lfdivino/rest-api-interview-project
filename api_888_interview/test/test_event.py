# -*- coding: utf-8 -*-

import unittest
from api_888_interview.app.core import core_app
from api_888_interview.app.db_event_commands import EventCommandsDB
from api_888_interview.test.constants import *


class TestEventUsingRoutes(unittest.TestCase):
    def setUp(self):
        self.api = core_app().test_client()

    def create_new_event(self):
        result = self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        self.assertEqual(
            result.json,
            994839351740,
            "Event can't be created!"
        )

    def create_new_event_without_send_json(self):
        result = self.api.post('/api/v1/event')
        self.assertEqual(
            result.json,
            "Invalid request json",
            "Error message not displayed!"
        )

    def create_event_that_exist_in_the_collection(self):
        result = self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        self.assertEqual(
            result.json,
            'The event id 994839351740 already exists!',
            'The event with the same id was created!'
        )

    def delete_event_by_id(self):
        event_db = EventCommandsDB()
        event_db.delete_event(JSON_NEW_EVENT['event']['id'])
        event_db.delete_event(JSON_NEW_EVENT_02['event']['id'])

    def test_create_event(self):
        self.create_new_event()
        self.create_new_event_without_send_json()
        self.create_event_that_exist_in_the_collection()
        self.delete_event_by_id()

    def update_odds_non_existed_event(self):
        result = self.api.post('/api/v1/odds', json=JSON_UPDATE_ODDS)
        self.assertEqual(
            result.json,
            "The event id 994839351740 don't exists!",
            "Update odds of a different event!"
        )

    def update_odds_without_send_json(self):
        result = self.api.post('/api/v1/odds')
        self.assertEqual(
            result.json,
            "Invalid request json",
            "Update odds of a non specified event!"
        )

    def update_odds_event(self):
        result_create = self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        result_update = self.api.post('/api/v1/odds', json=JSON_UPDATE_ODDS)
        self.assertTrue(
            result_update.json,
            'It was not possible to update this event odds!'
        )

    def test_update_odds(self):
        self.update_odds_non_existed_event()
        self.update_odds_without_send_json()
        self.update_odds_event()
        self.delete_event_by_id()

    def search_match_by_id(self):
        result_create = self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        result_search = self.api.get('/api/v1/match/994839351740')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_ID,
            "The result of the search by id is different "
            "from the event in the database"
        )

        result_search = self.api.get('/api/v1/match/231231312')
        self.assertEqual(
            result_search.json,
            "Match not found!",
            "The result of the search by non existing id find an event"
        )

    def search_match_by_name(self):
        result_search = self.api.get(
            '/api/v1/match/?name=Real Madrid vs Barcelona')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_NAME,
            "The result of the search by name is different "
            "from the event in the database"
        )

    def search_match_by_sport_and_ordering(self):
        result_search = self.api.get(
            '/api/v1/match/?sport=Football&ordering=startTime')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_SPORT,
            "The result of the search by sport is different "
            "from the event in the database"
        )

    def search_match_by_sport(self):
        result_search = self.api.get(
            '/api/v1/match/?sport=Football')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_SPORT,
            "The result of the search by sport is different "
            "from the event in the database"
        )

    def search_matchs(self):
        result_create = self.api.post('/api/v1/event', json=JSON_NEW_EVENT_02)
        result_search = self.api.get('/api/v1/match/')
        self.assertEqual(
            len(result_search.json),
            2,
            "The result of the search of all matches is different "
            "from the events in the database"
        )

    def test_match_search(self):
        self.search_match_by_id()
        self.search_match_by_name()
        self.search_match_by_sport_and_ordering()
        self.search_match_by_sport()
        self.search_matchs()
        self.delete_event_by_id()


if __name__ == '__main__':
    unittest.main()
