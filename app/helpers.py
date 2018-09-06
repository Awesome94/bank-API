from flask import jsonify, make_response, request, url_for

def response(status, message, status_code):
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code
