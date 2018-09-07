from app import db
from flask_bcrypt import Bcrypt
from enum import IntEnum, Enum
import jwt
from datetime import datetime, timedelta
from flask import current_app

class User(db.Model):
    __tablename__ = 'users'

    class Type(IntEnum):
        client = 1
        bank_teller = 2
        admin = 3

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password = db.Column(db.String(128))
    type = db.Column(db.SmallInteger, default=Type.client.value, nullable=False)
    id_type = db.Column(db.String, nullable=False)
    id_number = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)

    def __init__(self, email, firstname, lastname, password, id_type, id_number, phone_number):
        """Initialize the user with an email and a password."""
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.firstname = firstname
        self.lastname = lastname
        self.id_type = id_type
        self.id_number = id_number
        self.phone_number = phone_number

    def password_is_valid(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        """
        Save a user to the database.
        This includes creating a new user and editing one.
        """
        db.session.add(self)
        db.session.commit()

    def generate_token(self, user_id):
        """ Generates the access token"""

        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                current_app.config.get('SECRET'),
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    def get_user(id):
        return User.query.filter_by(id=id)

    def get_all():
        return User.query.all()

    def __repr__(self):
        return '<User {}>'.format(self.firstname)

class Accounts(db.Model):
    """Contains all the account details owned by the users"""
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String)
    account_number = db.Column(db.String(128))
    balance = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship(
        'User',
        backref=db.backref('accounts', lazy='dynamic'),
        uselist=False
    )

    def __init__(self, user_id, account_name, account_number):
        self.user_id = user_id
        self.account_name = account_name
        self.account_number = account_number

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_user_account(id):
        return Accounts.query.filter_by(user_id=id)

    def get_all():
        return Accounts.query.all()

    def __repr__(self):
        return '<Account balance {}>'.format(self.balance)

class Events(db.Model):
    """This will keep track of the various events that occur on the API"""
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String, unique=False, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_all():
        return Events.query().all()

    def __repr__(self):
        return '<Event {}>'.format(self.name)
