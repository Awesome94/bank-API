from app import db
from flask_bcrypt import Bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password = db.Column(db.String(128))
    user_type = db.Column(db.String(120), index=True)
    id_type = db.Column(db.String, nullable=False)
    id_number = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)

    def __init__(self, email, firstname, lastname, password, user_type, id_type, id_number, phone_number):
        """Initialize the user with an email and a password."""
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.firstname = firstname
        self.lastname = lastname
        self.user_type = user_type
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

    def get_all():
        return User.query.all()

    def __repr__(self):
        return '<User {}>'.format(self.firstname)

class Accounts(db.Model):
    """Contains all the account details owned by the users"""
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.Integer)
    balance = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, account_number, account_type, account_balance):
        self.account_type = account_type
        self.account_number = account_number
        self.account_balance = account_balance

    def save(self):
        db.session.add(self)
        db.session.commit()

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
