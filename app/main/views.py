from app.main import main_bp
from flask import request
from flask_login import login_required

@main_bp.route('/')
@login_required
def home():

    return "welcome to flask 101"

@main_bp.route('/profile')
@login_required
def profile():

    return "profile page"