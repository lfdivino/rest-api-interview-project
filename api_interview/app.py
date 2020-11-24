from flask import Flask

from api_interview.ext import database, serializer, documentation
from api_interview.blueprints import api


def create_app():
    app = Flask(__name__)
    database.init_app(app)
    api.init_app(app)
    serializer.init_app(app)
    documentation.init_app(app)

    return app
