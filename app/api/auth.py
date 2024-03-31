from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from app.models import User
from flask import current_app, jsonify
from werkzeug.security import check_password_hash

token_auth = HTTPTokenAuth()
basic_Auth = HTTPBasicAuth()


@basic_Auth.verify_password
def verify_password(email, password):

    user = User.query.filter_by(email = email).first()

    if not user or  not check_password_hash(user.password, password):

        return None
    
    return user

@token_auth.verify_token
def verify_token(token):

    jwt = User.verify_token(token, current_app.config['SECRET_KEY'])

    if jwt is None:

        return None
    
    return User.query.get(jwt["sub"])

@basic_Auth.error_handler
def basic_auth_error(status):

    return jsonify({'message': 'Invalid credentials'}), status


@token_auth.error_handler
def token_auth_error(status):

    return jsonify({'message': 'Unauthorized'}), status