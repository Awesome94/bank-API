from app.models import Accounts, User, Events
from marshmallow import Schema, fields, pprint

class UserSchema(Schema):
    firstname = fields.Str()
    firstname = fields.Str()
    id_number = fields.Int()
    phone_number = fields.Int()
    id_type = fields.Str()
    user_type = fields.Str()

class AccountSchema(Schema):
    email = fields.Str()
    account_type = fields.Str()
    account_number = fields.Int()
    balance = fields.Str()
    user_id = fields.Str()

user_schema = UserSchema()
user_schema = UserSchema(many=True)
