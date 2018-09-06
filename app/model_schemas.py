from app.models import Accounts, User, Events
from app import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'lastname','user_type','id_type','id_number','phone_number', 'firstname')

class AccountSchema(ma.Schema):
    class Meta:
        model = Accounts

user_schema = UserSchema()
user_schema = UserSchema(many=True)
