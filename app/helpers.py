from flask import jsonify, make_response, request, url_for, json
from app.models import User, Accounts
from app import db
import random

def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code

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


def withdraw(account_id):
    return "withdraw successful"

# def deposit(account_id):
#     account_number = request.json.get('account_number')
#     amount = request.json.get('amount')
#     client_id = request.json.get('user_id')
#     print(account_number, amount, client_id, account_id)
#     accounts = Accounts.get_all()
#     for account in accounts:
#         if client_id == account.user_id:
#             if account.account_number == account_number and account.id == id:
#                 account.balance = account.balance+amount
#                 account.Save()
#             else:
#                 return response('Transaction Denied', 'Try again', 401)
#
#         return "incorrect details"

def funds_transfer(account_id):
    return "funds transfer successful"

def check_balance(account_id):
    account = Accounts.query.filter_by(id=account_id)
    return "your balance is {account.balance} "
