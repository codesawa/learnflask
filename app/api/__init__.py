from flask import Blueprint

api_bp =Blueprint("api", __name__)

from app.api.views import *
from app.api.errors import *