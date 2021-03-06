from app.models import Accounts, User, Events
from app import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'lastname', 'id_type','id_number','phone_number', 'firstname')

class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'account_name', 'account_number', 'balance')

user_schema = UserSchema()
user_schema = UserSchema(many=True)

account_schema = AccountSchema()
account_schema  = AccountSchema(many=True)
