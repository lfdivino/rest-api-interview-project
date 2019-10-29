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
            8663424224,
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
            'The event id 8663424224 already exists!',
            'The event with the same id was created!'
        )

    def delete_event_by_id(self):
        event_db = EventCommandsDB()
        event_db.delete_event(JSON_NEW_EVENT['id'])

    def test_create_event(self):
        self.create_new_event()
        self.create_new_event_without_send_json()
        self.create_event_that_exist_in_the_collection()
        self.delete_event_by_id()


if __name__ == '__main__':
    unittest.main()
