from flask import jsonify, make_response, request, url_for, json
from app.models import User, Accounts
from app import db, app
import random
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
            current_user = User.query.filter_by(id=data['sub']).first()
            print(current_user)
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

def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code

def generate_account_number():
  account_numbers = Accounts.get_all()
  rand_account_number = random.randint(10000000000,10000039999)
  if rand_account_number not in account_numbers:
    new_account_number = '11'+ f'{rand_account_number}'
    return new_account_number
  else:
    return generate_account_number()
