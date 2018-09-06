from app import app, models
from flask.views import MethodView
from app.helpers import response


class Login(MethodView):
    def post(self):
        return "login successful"
        pass

class LogOut(MethodView):
    def post(self):
        return "logout successful"
        pass

def register():
    return "got it"

class User(MethodView):

    def get(self, user_id):
        if user_id is None:
            print(user_id)
            return "all users"
        else:
            print(user_id)
            return "one users"

    def post(self):
        return "user created"
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass


class Account(MethodView):
    def get(self, account_id):
        if account_id:
            return "one account"
        else:
            return "all accounts"
        pass

    def delete(self, account_id):
        return "account deleted"

    def post(self):
        return "account created"
        pass

    # def post('v1/', account_id):
    #     return "account created"
    #     pass

    def put(self, account_id):
        pass


# register = User.as_view('register')
auth_view = Login.as_view('authentication')
app.add_url_rule('/v1/login',view_func=auth_view, methods=['POST'])

end_view = LogOut.as_view('end_session')
app.add_url_rule('/v1/logout',view_func=end_view, methods=['POST'])

user_view = User.as_view('user_api')
app.add_url_rule('/v1/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET'])

app.add_url_rule('/v1/register', view_func=user_view, methods=['POST'])
app.add_url_rule('/v1/register/all', view_func=register, methods=['POST'])
app.add_url_rule('/v1/users/<int:user_id>', view_func=user_view, methods=['GET'])

accounts_view = Account.as_view('accounts_api')
app.add_url_rule('/v1/accounts/', defaults={'account_id': None},
                 view_func=accounts_view, methods=['GET'])
app.add_url_rule('/v1/accounts/', view_func=user_view, methods=['POST'])
app.add_url_rule('/v1/account/<int:account_id>', view_func=user_view, methods=['GET'])


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
