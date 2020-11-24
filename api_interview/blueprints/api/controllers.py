from pymongo import ASCENDING
from marshmallow import ValidationError

from api_interview.ext.database import mongo
from api_interview.ext.serializer import NewMessageSchema, EventSchema, \
    MatchSchema


def _get_event_by_id(event_id):
    return mongo.db.events.find_one_or_404({"id": int(event_id)}, {"_id": 0})


def create_event(json):
    """Function responsible to verify if the ```Èvent``` already exist,
    if False, call the Event database function to create a new on"""
    try:
        new_message_schema = NewMessageSchema()
        event = new_message_schema.load(json)
        event_obj = mongo.db.events.find_one({"id": event['event']['id']})

        if event_obj:
            return 'The event id {} already exists!'.format(
                event['event']['id']), 400

        event["event"]["url"] = \
            "/api/v1/match/{}".format(event["event"]["id"])

        mongo.db.events.insert_one(event["event"])

        return json['event']['id'], 201
    except ValidationError as err:
        return err.messages, 400


def get_events():
    """Return all the events in the collection"""
    event = mongo.db.events.find()
    event_schema = EventSchema(many=True)

    return event_schema.dump(event), 200


def get_event_by_id(event_id):
    """Return the match by its 'id'"""
    event_schema = EventSchema()
    event = _get_event_by_id(int(event_id))

    return event_schema.dump(event), 200


def get_event_by_name(name):
    """Return the match by its 'name'"""
    match_schema = MatchSchema()
    event = mongo.db.events.find_one({'name': name})

    return match_schema.dump(event), 200


def get_event_by_sport(sport, ordering=None):
    events = None
    match_schema = MatchSchema(many=True)

    if ordering:
        events = mongo.db.events.find({'sport.name': sport}).sort(
            [(ordering, ASCENDING)])
    else:
        events = mongo.db.events.find({'sport.name': sport})

    return match_schema.dump(events), 200


def update_odds_json_event(json, event):
    """Function responsible for updating the Odds in the ```Event```
    object and returning this modified event"""
    for selection in json['markets'][0]['selections']:
        for event_selection in event['markets'][0]['selections']:
            if event_selection['id'] == selection['id']:
                event_selection['odds'] = selection['odds']

    return event


def update_odds(event_id, json):
    """Function responsible for validate if the ```Event```, them call
    the function to update the values and update the collection in the
    database"""
    event = _get_event_by_id(int(event_id))

    json_modified_odds = update_odds_json_event(json['event'], event)

    mongo.db.events.update_one(
        {'id': event['id']},
        {'$set': json_modified_odds}
    )

    return {}, 204
