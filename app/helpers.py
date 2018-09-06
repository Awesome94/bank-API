from flask import jsonify, make_response, request, url_for, json
from app.models import User

def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code

def register():
    # query if the user exists
    print("this is final call", data)
    user = User.query.filter_by(email=request.json.get('email')).first()

    if not user:
        try:
            post_data = request.json
            # register the user
            email = post_data.get('email')
            firstname = post_data.get('firstname')
            lastname = post_data.get('lastname')
            password_hash = post_data.get('password_hash')
            user_type = post_data.get('user_type')
            id_type = post_data.get('id_type')
            id_number = post_data.get('id_number')
            phone_number = post_data.get('phone_number')
            user = User(email=email, firstname=firstname, lastname=lastname,
                    password_hash=password_hash, user_type=user_type,
                    id_type=id_type, id_number=id_number, phone_number=phone_number
            )
            user.save()
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



    return "got it"

def withdraw(account_id):
    return "withdraw successful"

def deposit(account_id):
    return "withdraw successful"

def funds_transfer(account_id):
    return "funds transfer successful"

def check_balance(account_id):
    return "you have no balance"
