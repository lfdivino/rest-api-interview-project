# -*- coding: utf-8 -*-

from .event import NewEvent


def add_routes(api):
    api.add_resource(NewEvent, '/api/v1/event')
