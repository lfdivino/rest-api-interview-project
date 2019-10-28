# -*- coding: utf-8 -*-

import unittest
from app.core import core_app
from .constants import *


class TestEventUsingRoutes(unittest.TestCase):
    def setUp(self):
        self.api = core_app().test_client()

    def test_create_new_event(self):
        result = self.api.post('/api/v1/event', json=JSON_NEW_EVENT)
        self.assertEqual(
            result.json,
            8663424224,
            "Event can't be created!"
        )

    def test_create_new_event_without_send_json(self):
        result = self.api.post('/api/v1/event')
        self.assertEqual(
            result.json,
            'Invalid request json',
            "Error message not displayed!"
        )


if __name__ == '__main__':
    unittest.main()
