from flask import jsonify, make_response, request, url_for

def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code

def register():
    return "got it"

def withdraw(account_id):
    return "withdraw successful"

def deposit(account_id):
    return "withdraw successful"

def funds_transfer(account_id):
    return "funds transfer successful"

def check_balance(account_id):
    return "you have no balance"
