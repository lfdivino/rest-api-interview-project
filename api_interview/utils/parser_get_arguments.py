# -*- coding: utf-8 -*-
from flask_restful import reqparse


def parser_get_arguments():
    """Collect the parameters from the Querystring in the GET requests

    :rtype: A dictionary of parameters"""
    parser = reqparse.RequestParser()
    parser.add_argument('name', location='args')
    parser.add_argument('sport', location='args')
    parser.add_argument('ordering', location='args')

    return parser
