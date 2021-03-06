from app import app, db
from app.models import Accounts, User, Events
from app.model_schemas import user_schema, account_schema
from flask.views import MethodView
from app.helpers import response, token_required, generate_account_number
from flask import Flask, jsonify, request, make_response
import jwt
import uuid
from app.data import data

@app.route('/', methods=['GET'])
def load_home_page():
    return jsonify({
        '/v1': data
    }), 200

@app.route('/v1/register', methods=['POST'])
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

@app.route('/v1/login', methods=['POST'])
def login_user():
    try:
        # Get the user object using their email
        user = User.query.filter_by(email=request.json.get('email')).first()

        # Try to authenticate the found user using their password
        if user and user.password_is_valid(request.json.get('password')):
            # Generate the access token. This will be used as the authorization header

            access_token = user.generate_token(user.id)

            if access_token:
                print(access_token)
                response = {
                    'message': 'You logged in successfully.',
                    'access_token': access_token.decode()
                }
                return make_response(jsonify(response)), 200
        else:
            # User does not exist. so error message
            response = {
                'message': 'Invalid email or password, Please try again'
            }
            return make_response(jsonify(response)), 401

    except Exception as e:
        # Create a response containing an string error message
        response = {
            'message': str(e)
        }
        # Return a server error using the HTTP Error Code 500 (Internal Server Error)
        return make_response(jsonify(response)), 500

@app.route('/v1/logout', methods=['POST'])
def log_out(self):
    return "logout successful"

@app.route('/v1/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        return response('unauthorised', 'Cannot perform operation', 401)
    all_users = User.get_all()
    result = user_schema.dump(all_users)
    return jsonify(result.data)

@app.route('/v1/users/<user_id>/', methods=['GET'])
@token_required
def get_one_user(current_user, user_id):
    """
    only admin user can get any user by id. normal users can only get there profile
    """
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        user = db.session.query(User).filter_by(id=current_user.id)
        result = user_schema.dump(user)
        return jsonify(result.data)
    else:
        user = db.session.query(User).filter_by(id=user_id)
        result = user_schema.dump(user)
        return jsonify(result.data)

@app.route('/v1/users/<user_id>/', methods=['DELETE'])
@token_required
def delete_one_user(current_user, user_id):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        return response('unauthorised', 'Cannot perform operation', 401)
    if not user:
        return jsonify({"message: no User found"})
    User.delete_user(id)
    return jsonify({'message': 'user {user_id} deleted successfully'})

@app.route('/v1/users/<user_id>/', methods=['PUT'])
@token_required
def change_use_type(current_user, user_id):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        return response('unauthorised', 'Cannot perform operation', 401)
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return response('Not found', 'user not found check ID', 404)
    user.type = request.json.get('type')
    db.session.commit()
    return response('success', 'user status updated', 200)


@app.route('/v1/accounts/all', methods=['GET'])
@token_required
def load_all_accounts(current_user):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        return response('unauthorised', 'Cannot perform operation', 401)
    all_accounts = Accounts.get_all()
    result = account_schema.dump(all_accounts)
    return jsonify(result.data)


@app.route('/v1/accounts/<account_id>', methods=['GET'])
@token_required
def get_account(current_user, account_id):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        user_account = Accounts.get_user_account(current_user.id)
        result = account_schema.dump(user_account)
        return jsonify(result.data)
    else:
        account = Accounts.query.filter_by(id=account_id)
        result = account_schema.dump(account)
        return jsonify(result.data)


@app.route('/v1/accounts/<account_id>', methods=['DELETE'])
def delete(self, account_id):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        return response('unauthorised', 'Cannot perform operation', 401)
    Accounts.delete_account(account_id)
    return jsonify({'message': 'user {account_id} deleted successfully'})


@app.route('/v1/accounts/deposit/<account_id>', methods=['PUT'])
@token_required
def deposit_to_account(current_user, account_id):
    if int(current_user.type)!=User.Type.admin or int(current_user.type)!=User.Type.bank_teller:
        return response('unauthorised', 'Cannot perform operation', 401)
    if account_id is not None:
        account_number = request.json.get('account_number')
        amount = request.json.get('amount')
        client_id = request.json.get('user_id')
        account = Accounts.query.filter_by(account_number=account_number, user_id=client_id).first()
        if account:
            amount_to_deposit = (int(amount))
            account.balance = account.balance + amount_to_deposit
            account.save()
            account = Account.get_user_account(current_user.id)
            result = account_schema.dump(account)
            return jsonify(result.data)
        return "invalid account details do not match"


@app.route('/v1/accounts/withdraw/<account_id>', methods=['PUT'])
@token_required
def withdraw(current_user, account_id):
    if account_id is not None:
        account_number = request.json.get('account_number')
        amount = request.json.get('amount')
        account = Accounts.query.filter_by(account_number=account_number, user_id=current_user.id).first() ## TODO: modify query to get current users account
        if account:
            amount_to_withdraw = (int(amount))
            if amount_to_withdraw > account.balance:
                return "cannot withdraw more than balance"
            else:
                account.balance = account.balance - amount_to_withdraw
                account.save()
                account = Accounts.get_user_account(current_user.id)
                result = account_schema.dump(account)
                return jsonify(result.data)


@app.route('/v1/accounts/transfer/<account_id>', methods=['PUT'])
@token_required
def funds_transfer(current_user, account_id):
    if account_id is not None:
        account_number =  request.json.get('account_number')
        amount = request.json.get('amount')
        pin = request.json.get('pin')
        account = Accounts.query.filter_by(user_id=current_user.id).first() ## TODO: modify query to get current users account
        reciever_account = Accounts.query.filter_by(account_number=account_number).first() ## TODO: modify query to get current users account

        if account and reciever_account:
            amount_to_transfer = (int(amount))
            if amount_to_transfer > account.balance:
                return response('failed', 'cannot transfer more than balance', 403)
            else:
                account.balance = account.balance - amount_to_transfer
                reciever_account.balance = reciever_account.balance + amount_to_transfer
                account.save()
                reciever_account.save()
                return ({"message": "Transaction successful"})
        return ({"message": "funds transfer unsuccessful"})


@app.route('/v1/accounts/balance/<account_id>', methods=['GET'])
@token_required
def check_balance(current_user, account_id):
    if account_id:
        account = Accounts.query.filter_by(id=account_id, user_id=current_user.id)
        result = account_schema.dump(account)
        return jsonify(result.data)
    return response('failed', 'check account id and try again', 200)

def put(self, account_id):
    return "account updated"
    pass
