# -*- coding: utf-8 -*-
from flask import request
from flask_restful import reqparse


def get_request_json():
    json_args = request.get_json()

    if not json_args:
        return False

    return json_args


def parser_get_arguments():
    parser = reqparse.RequestParser()
    parser.add_argument('name', location='args')
    parser.add_argument('sport', location='args')
    parser.add_argument('ordering', location='args')

    return parser
