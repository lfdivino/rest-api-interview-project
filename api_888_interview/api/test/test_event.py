# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from ..app import app
from .constants import *


class TestEventUsingRoutes(unittest.TestCase):
    def setUp(self):
        self.api = app.test_client()

    @patch('api_888_interview.api.src.database.db_event.DBEvent.create_event')
    def create_new_event(self, mock_create_event):
        mock_create_event.return_value = CREAETE_NEW_EVENT
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

    @patch('api_888_interview.api.src.database.db_event.DBEvent.select_event_by_id')
    def create_event_that_exist_in_the_collection(
            self, mock_select_event_by_id):
        mock_select_event_by_id.return_value = JSON_NEW_EVENT['event']
        result = self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        self.assertEqual(
            result.json,
            'The event id 994839351740 already exists!',
            'The event with the same id was created!'
        )

    def test_create_event(self):
        self.create_new_event()
        self.create_new_event_without_send_json()
        self.create_event_that_exist_in_the_collection()

    @patch('api_888_interview.api.src.database.db_event.DBEvent.select_event_by_id')
    def update_odds_non_existed_event(self, mock_select_event_by_id):
        mock_select_event_by_id.return_value = None
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

    @patch('api_888_interview.api.src.database.db_odds.DBOdds.update_odds')
    @patch('api_888_interview.api.src.database.db_event.DBEvent.select_event_by_id')
    def update_odds_event(self, mock_event_by_id, mock_update_odds):
        mock_event_by_id.return_value = CREAETE_NEW_EVENT['event']
        mock_update_odds.return_value = UPDATE_ODDS
        result_update = self.api.post('/api/v1/odds', json=JSON_UPDATE_ODDS)
        self.assertTrue(
            result_update.json,
            'It was not possible to update this event odds!'
        )

    def test_update_odds(self):
        self.update_odds_non_existed_event()
        self.update_odds_without_send_json()
        self.update_odds_event()

    @patch('api_888_interview.api.src.database.db_event.DBEvent.select_event_by_id')
    @patch('api_888_interview.api.src.database.db_event.DBEvent.create_event')
    def search_match_by_id(self, mock_create_event, mock_select_event_by_id):
        mock_create_event.return_value = CREAETE_NEW_EVENT
        mock_select_event_by_id.return_value = JSON_EVENT_BY_ID
        self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        result_search = self.api.get('/api/v1/match/994839351740')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_ID,
            "The result of the search by id is different "
            "from the event in the database"
        )

        mock_select_event_by_id.return_value = None

        result_search = self.api.get('/api/v1/match/231231312')
        self.assertEqual(
            result_search.json,
            "Match not found!",
            "The result of the search by non existing id find an event"
        )

    @patch('api_888_interview.api.src.database.db_match.DBMatch.select_event_by_name')
    def search_match_by_name(self, mock_event_by_name):
        mock_event_by_name.return_value = JSON_EVENT_BY_NAME
        result_search = self.api.get(
            '/api/v1/match/?name=Real Madrid vs Barcelona')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_NAME,
            "The result of the search by name is different "
            "from the event in the database"
        )

    @patch('api_888_interview.api.src.database.db_match.DBMatch.select_event_by_sport')
    def search_match_by_sport_and_ordering(self, mock_event_by_sport):
        mock_event_by_sport.return_value = JSON_EVENT_BY_SPORT
        result_search = self.api.get(
            '/api/v1/match/?sport=Football&ordering=startTime')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_SPORT,
            "The result of the search by sport is different "
            "from the event in the database"
        )

    @patch('api_888_interview.api.src.database.db_match.DBMatch.select_event_by_sport')
    def search_match_by_sport(self, mock_event_by_sport):
        mock_event_by_sport.return_value = JSON_EVENT_BY_SPORT
        result_search = self.api.get(
            '/api/v1/match/?sport=Football')
        self.assertEqual(
            result_search.json,
            JSON_EVENT_BY_SPORT,
            "The result of the search by sport is different "
            "from the event in the database"
        )

    @patch('api_888_interview.api.src.database.db_match.DBMatch.select_events')
    def search_matchs(self, mock_select_matches):
        mock_select_matches.return_value = [JSON_NEW_EVENT, JSON_NEW_EVENT_02]
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


if __name__ == '__main__':
    unittest.main()
