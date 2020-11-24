import json

from test.constants import *


def test_create_new_event_missing_required_fields(client):
    result = client.post('/api/v1/event/', json=JSON_NEW_EVENT_MISSING_FIELDS)

    assert result.json == {'event': {'id': ['Missing data for required field.'], 'name': ['Missing data for required field.']}}
    assert result.status == "400 BAD REQUEST"


def test_create_new_event_wrong_date_pattern(client):
    result = client.post('/api/v1/event/', json=JSON_NEW_EVENT_DATE_WRONG_PATTERN)

    assert result.json == {'event': {'startTime': ['Invalid value.']}}
    assert result.status == "400 BAD REQUEST"


def test_create_new_event(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find_one',
        return_value=None
    )
    mocker.patch(
        'pymongo.collection.Collection.insert_one',
        return_value={"json": 994839351740, "status": "201 CREATED"}
    )
    result = client.post('/api/v1/event/', json=JSON_NEW_EVENT)

    assert result.json == 994839351740
    assert result.status == "201 CREATED"


def test_create_new_event_without_send_json(client):
    result = client.post('/api/v1/event/')

    assert result.json == "Invalid request json"
    assert result.status == "400 BAD REQUEST"


def test_create_event_that_exist_in_the_collection(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find_one',
        return_value={"json": "The event id 994839351740 already exists!", "status": "400 BAD REQUEST"}
    )
    result = client.post('/api/v1/event/', json=JSON_NEW_EVENT)

    assert result.json == 'The event id 994839351740 already exists!'
    assert result.status == "400 BAD REQUEST"


def test_update_odds_non_existed_event(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find_one_or_404',
        return_value={"json": {'message': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}, "status": "404 NOT FOUND"}
    )
    result = client.put('/api/v1/odds/994839351741', json=JSON_UPDATE_ODDS)

    assert result.json == {'message': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}
    assert result.status == "404 NOT FOUND"


def test_update_odds_without_send_json(client):
    result = client.put('/api/v1/odds/994839351740')

    assert result.json == "Invalid request json"
    assert result.status == "400 BAD REQUEST"


def test_update_odds_event(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.update_one',
        return_value={"status": "204 NO CONTENT"}
    )
    result = client.put('/api/v1/odds/994839351740', json=JSON_UPDATE_ODDS)

    assert result.status == "204 NO CONTENT"


def test_search_match_by_id(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find_one_or_404',
        return_value={"status": "200 OK"}
    )
    result = client.get('/api/v1/match/994839351740')

    assert result.json == UPDATE_ODDS
    assert result.status == "200 OK"

    mocker.patch(
        'pymongo.collection.Collection.find_one_or_404',
        return_value={"json": {'message': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'},"status": "404 NOT FOUND"}
    )
    result = client.get('/api/v1/match/231231312')

    assert result.json == {'message': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}
    assert result.status == "404 NOT FOUND"


def test_search_match_by_name(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find_one',
        return_value={"json": JSON_EVENT_BY_NAME, "status": "200 OK"}
    )
    result = client.get(
        '/api/v1/match/?name=Real Madrid vs Barcelona')

    assert result.json == JSON_EVENT_BY_NAME
    assert result.status == "200 OK"


def test_search_match_by_sport_and_ordering(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find',
        return_value={"json": JSON_EVENT_BY_SPORT, "status": "200 OK"}
    )
    result = client.get('/api/v1/match/?sport=Football&ordering=startTime')
    print(result)
    assert result.json == JSON_EVENT_BY_SPORT
    assert result.status == "200 OK"


def test_search_match_by_sport(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find',
        return_value={"json": JSON_EVENT_BY_SPORT, "status": "200 OK"}
    )
    result = client.get('/api/v1/match/?sport=Football')
    print(result)

    assert result.json == JSON_EVENT_BY_SPORT
    assert result.status == "200 OK"


def test_search_matchs(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find',
        return_value={"json": JSON_ALL_MATCHS, "status": "200 OK"}
    )
    result = client.get('/api/v1/match/')

    assert len(result.json) == 2
    assert result.status == "200 OK"


def test_get_all_events(client, mocker):
    mocker.patch(
        'pymongo.collection.Collection.find',
        return_value={"json": ALL_EVENTS, "status": "200 OK"}
    )
    result = client.get('api/v1/events/')

    assert len(result.json) == 2
    assert result.status == "200 OK"
