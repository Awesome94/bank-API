from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(120), index=True)
    id_type = db.Column(db.String, nullable=False)
    id_number = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)

class Accounts(db.Model):
    """Contains all the account details owned by the users"""
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    account_type = db.Column(db.String(120), index=True)
    account_number = db.Column(db.Integer)
    balance = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Events(db.Model):
    """This will keep track of the various events that occur on the API"""
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String, unique=False, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
