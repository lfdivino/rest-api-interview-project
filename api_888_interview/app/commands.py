# -*- coding: utf-8 -*-
from flask import request
from flask_restful import reqparse


def get_request_json():
    """Collect the json from the POST request and validate it exists

    :rtype: A JSON from the body of the POST request"""
    json_args = request.get_json()

    if not json_args:
        return False

    return json_args


def parser_get_arguments():
    """Collect the parameters from the Querystring in the GET requests

    :rtype: A dictionary of parameters"""
    parser = reqparse.RequestParser()
    parser.add_argument('name', location='args')
    parser.add_argument('sport', location='args')
    parser.add_argument('ordering', location='args')

    return parser
