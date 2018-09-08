from flask import jsonify, make_response, request, url_for, json
from app.models import User, Accounts
from app import db, app
import random
import hashlib
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            print(data)
            current_user = User.query.filter_by(id=data['sub'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/v1/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})

@app.route('/v1/protected')
@token_required
def protected():
    return jsonify({'message': 'For people with valid tokens!'})

def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code

@app.errorhandler(404)
def route_not_found(e):
    return response('failed', 'Endpoint not found', 404)

@app.errorhandler(405)
def method_not_found(e):
    """
    Custom response for methods not allowed for the requested URLs
    """
    return response('failed', 'The method is not allowed for the requested URL', 405)

@app.errorhandler(500)
def internal_server_error(e):
    """
    Return a custom message for a 500 internal error
    """
    return response('failed', 'Internal server error', 500)

def valid_password(userid, password):
    user = get_user(userid)
    pw_hash = hashlib.sha256(password).hexdigest()
    if user.hash == pw_hash:
        return True
    return False

def register():
    # query if the user exists
    user = User.query.filter_by(email=request.json.get('email')).first()

    if not user:
        try:
            post_data = request.json
            # register the user
            email = post_data.get('email')
            firstname = post_data.get('firstname')
            lastname = post_data.get('lastname')
            password = post_data.get('password')
            user_type = post_data.get('user_type')
            id_type = post_data.get('id_type')
            id_number = post_data.get('id_number')
            phone_number = post_data.get('phone_number')
            user = User(email=email, firstname=firstname, lastname=lastname,
                    password=password,
                    id_type=id_type, id_number=id_number, phone_number=phone_number
            )
            user.save()
            account_name  = firstname+ ' ' +lastname
            account=Accounts(user_id=user.id, account_name=account_name, account_number=generate_account_number())
            account.save()
            return response('success', 'account created', 201)
        except Exception as e:
            #In case of any errors, return a String message containing the error
            result = {
                'message': str(e)
            }
            return make_response(jsonify(result)), 401
    else:
        # User is Already in the database so we do not want to register them twice
        return response('Already exists', 'Please Login', 202)

def generate_account_number():
  account_numbers = Accounts.get_all()
  rand_account_number = random.randint(10000000000,10000039999)
  if rand_account_number not in account_numbers:
    new_account_number = '11'+ f'{rand_account_number}'
    return new_account_number
  else:
    return generate_account_number()

@token_required
def change_use_type(current_user, _id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"No User found"})
    user.type = request.json(type)
    db.session.commit()
    return jsonify({"user status has been updated"})

def delete_user(userid):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message: no User found"})
    db.session.delete(user)
    db.session.commit()


def withdraw(account_id):
    if account_id is not None:
        account_number = request.json.get('account_number')
        amount = request.json.get('amount')
        pin = request.json.get('pin')
        account = Accounts.query.filter_by(account_number=account_number).first() ## TODO: modify query to get current users account
        if account:
            amount_to_withdraw = (int(amount))
            if amount_to_withdraw > account.balance:
                return "cannot withdraw more than balance"
            else:
                account.balance = account.balance - amount_to_withdraw
                account.save()
                return "Transaction successful"

def funds_transfer(account_id):
    return "funds transfer successful"

def check_balance(account_id):
    account = Accounts.query.filter_by(id=account_id)
    return "your balance is {account.balance} "
