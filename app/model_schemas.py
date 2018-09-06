from app.models import Accounts, User, Events
from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'date_created', 'firstname')

class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Accounts

user_schema = UserSchema()
user_schema = UserSchema(many=True)
