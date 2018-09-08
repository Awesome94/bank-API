from app import app, db
from app.models import Accounts, User, Events
from app.model_schemas import user_schema, AccountSchema
from flask.views import MethodView
from app.helpers import response, register, withdraw, check_balance, token_required
from flask import Flask, jsonify, request, make_response
import jwt
from app.data import data

class HomeView(MethodView):
    def get(self):
        return jsonify({
            '/v1': data
        }), 200

class LoginView(MethodView):
    def post(self):
        auth = request.authorization
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

class LogOut(MethodView):
    def post(self):
        return "logout successful"
        pass

class UserView(MethodView):
    decorators = [token_required]
    def get(current_user, self, user_id):
        if user_id is None:
            all_users = User.get_all()
            result = user_schema.dump(all_users)
            return jsonify(result.data)
        else:
            user = db.session.query(User).filter_by(id=user_id)
            result = user_schema.dump(user)
            return jsonify(result.data)

    def post(self):
        return "user created"
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass


class AccountView(MethodView):
    def get(self, account_id):
        if account_id:
            return "one account"
        else:
            return "all accounts"
        pass

    def delete(self, account_id):
        return "account deleted"

    def post(self, account_id):
        if account_id is not None:
            account_number = request.json.get('account_number')
            amount = request.json.get('amount')
            client_id = request.json.get('user_id')
            account = Accounts.query.filter_by(account_number=account_number, user_id=client_id).first()
            if account:
                amount_to_deposit = (int(amount))
                account.balance = account.balance + amount_to_deposit
                account.save()
                return "balance updated"
            return "invalid account details do not match"

    def put(self, account_id):
        return "account updated"
        pass


# register = User.as_view('register')
home_view = HomeView.as_view('home')
app.add_url_rule('/',view_func=home_view, methods=['GET'])

auth_view = LoginView.as_view('authentication')
app.add_url_rule('/v1/login',view_func=auth_view, methods=['POST'])

end_view = LogOut.as_view('end_session')
app.add_url_rule('/v1/logout',view_func=end_view, methods=['POST'])

user_view = UserView.as_view('user_api')
app.add_url_rule('/v1/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET'])

app.add_url_rule('/v1/register', view_func=register, methods=['POST'])
app.add_url_rule('/v1/users/<int:user_id>', view_func=user_view, methods=['GET'])

accounts_view = AccountView.as_view('accounts_api')
app.add_url_rule('/v1/accounts/', defaults={'account_id': None},
                 view_func=accounts_view, methods=['GET'])

app.add_url_rule('/v1/accounts/',
                 view_func=user_view, methods=['POST'])

app.add_url_rule('/v1/account/<int:account_id>',
                 view_func=user_view, methods=['GET'])

app.add_url_rule('/v1/account/withdraw/<int:account_id>',
                 view_func=withdraw, methods=['POST'])

app.add_url_rule('/v1/account/<int:account_id>/balance',
                 view_func=check_balance, methods=['GET'])

app.add_url_rule('/v1/account/deposit/<int:account_id>',
                 view_func=accounts_view, methods=['POST'])
