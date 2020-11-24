# -*- coding: utf-8 -*-
from flask import request


def get_request_json():
    """Collect the json from the POST request and validate it exists

    :rtype: A JSON from the body of the POST request"""
    json_args = request.get_json()

    if not json_args:
        return False

    return json_args
