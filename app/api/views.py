from app.api import api_bp
from app.api.auth import basic_Auth, token_auth
from flask import jsonify
from app.models import User

@api_bp.route('/login')
@basic_Auth.login_required
def login():

    current_user = basic_Auth.current_user()


    token = current_user.generate_auth_token()

    return jsonify({'token': token})


@api_bp.route('/users')
@token_auth.login_required
def get_users():

    users = {}

    for userset in User.query.all():

        users['email'] = userset.email
        users['name'] = userset.name

    return jsonify({'users': users})