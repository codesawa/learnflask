from app.api import api_bp
from flask import jsonify

@api_bp.app_errorhandler(500)
def server_error(_):
    return jsonify({"message": "Its not you it's us"}), 500


@api_bp.app_errorhandler(404)
def not_found(_):
    return jsonify({"message": "Not found"}), 404