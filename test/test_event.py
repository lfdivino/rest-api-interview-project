# -*- coding: utf-8 -*-

import unittest
from app.core import core_app
from test.constants import *
from app.db_event_commands import EventCommandsDB


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


if __name__ == '__main__':
    unittest.main()
