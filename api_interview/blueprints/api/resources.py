from flasgger import swag_from
from flask_restful import Resource

from api_interview.utils.get_request_json import get_request_json
from api_interview.utils.parser_get_arguments import parser_get_arguments

from .controllers import create_event, get_events, get_event_by_id, \
    get_event_by_name, get_event_by_sport, update_odds


class Event(Resource):
    """Class responsible for managing the routes of the NewEvents"""
    @swag_from("documentation/event_post.yml")
    def post(self):
        """Function responsible to receive the POST request and start the
        Create a new Event"""
        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return create_event(json_args)


class Events(Resource):
    """Class responsible for managing the routes to return all events"""
    @swag_from("documentation/event_get.yml")
    def get(self):

        return get_events()


class MatchByID(Resource):
    """Class responsible for managing the routes of search matches by id"""
    @swag_from("documentation/match_by_id_get.yml")
    def get(self, event_id=None):

        return get_event_by_id(event_id)


class MatchByArgs(Resource):
    """Class responsible for managing the routes of search matches
    by parameters"""
    @swag_from("documentation/matches_get.yml")
    def get(self):

        parser = parser_get_arguments()
        args = parser.parse_args()

        if args.get('name'):
            return get_event_by_name(args['name'])

        if args.get('sport'):
            return get_event_by_sport(args['sport'], args['ordering'])

        return get_events()


class Odds(Resource):
    """Class responsible for managing the update of the Event's Odds"""
    @swag_from("documentation/odd_put.yml")
    def put(self, event_id):

        json_args = get_request_json()

        if not json_args:
            return 'Invalid request json', 400

        return update_odds(event_id, json_args)
