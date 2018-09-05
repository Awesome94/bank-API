from app import app, models
from flask.views import MethodView
from app.helpers import response

class User(MethodView):
    def get(self):
        users = models.User.query.all()
        return "users"
        
class Accounts(MethodView):
    def get(self):
        pass

app.add_url_rule('/users/', view_func=User.as_view('users'))

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
