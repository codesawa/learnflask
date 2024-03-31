from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime, timedelta
from flask import current_app
import jwt

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(300))

    def generate_auth_token(self, timeline= 900):

        payload = {
            'exp': datetime.utcnow() + timedelta(seconds=timeline),
            'iat': datetime.utcnow(),
            'sub': self.id
        }

        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    

    @staticmethod
    def verify_token(token, secret_key):

        try:

            return jwt.decode(token, secret_key, algorithms=["HS256"])

        except:

            return None