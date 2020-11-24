from flask import Flask, Blueprint
from flask_restful import Api

from .resources import Event, Events, MatchByID, MatchByArgs, Odds

bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app: Flask):
    """Function responsible for group all the routes of the API"""
    api.add_resource(Event, '/event/')
    api.add_resource(Events, '/events/')
    api.add_resource(MatchByID, '/match/<event_id>')
    api.add_resource(MatchByArgs, '/match/')
    api.add_resource(Odds, '/odds/<event_id>')
    app.register_blueprint(bp)
