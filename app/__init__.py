from flask import Flask
from config import environment_config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()

login_manager = LoginManager()

from app.models import User


migrate = Migrate()


def create_app(env_config: str) ->Flask:

    app = Flask(__name__)

    app.config.from_object(environment_config[env_config])

    # flask ported service registration

    db.init_app(app=app)

    migrate.init_app(app=app, db=db)

    login_manager.login_view = "auth.login"

    login_manager.init_app(app=app)

    # partial initialization

    environment_config[env_config].init_app(app=app)

    # blueprint registration

    from app.main import main_bp
    from app.auth import auth_bp
    from app.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    app.register_blueprint(api_bp, url_prefix="/api")
    
    return app