# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from .src.routes.routes import add_routes


def init():
    app = Flask(__name__)
    api = Api(app)
    add_routes(api)

    return app


app = init()
