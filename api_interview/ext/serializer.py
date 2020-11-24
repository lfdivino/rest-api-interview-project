from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate


ma = Marshmallow()


def init_app(app: Flask):
	ma.init_app(app)


def validate_date(date_field):
	import re
	r = re.compile('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
	if r.match(date_field) is not None:
		return True

	return False


class SportSchema(ma.Schema):
	id = fields.Int(required=True)
	name = fields.Str(required=True)


class SelectionSchema(ma.Schema):
	id = fields.Int(required=True)
	name = fields.Str(required=True)
	odds = fields.Float(required=True)


class MarketSchema(ma.Schema):
	id = fields.Int(required=True)
	name = fields.Str(required=True)
	selections = fields.List(fields.Nested(SelectionSchema))


class EventSchema(ma.Schema):
	id = fields.Int(required=True)
	name = fields.Str(required=True)
	startTime = fields.Str(required=True, validate=validate_date)
	url = fields.Url()
	sport = fields.Nested(SportSchema)
	markets = fields.List(fields.Nested(MarketSchema))


class MatchSchema(ma.Schema):
	id = fields.Int()
	url = fields.Url()
	name = fields.Str()
	startTime = fields.Str()


class MessageSchema(ma.Schema):
	id = fields.Int(required=True)
	event = fields.Nested(EventSchema)


class NewMessageSchema(MessageSchema):
	message_type = fields.String(required=True, validate=validate.OneOf(["NewEvent"]))


class UpdateMessageSchema(MessageSchema):
	message_type = fields.String(required=True, validate=validate.OneOf(["UpdateOdds"]))
