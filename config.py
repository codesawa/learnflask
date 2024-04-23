import os
from flask import Flask
from redis import Redis
from rq import Queue
"""

Environments:
    Development
    Testing Environment
        LocalTesting
        CI_CD_Environment
    
    Production Environment

        HerokuEnvironment
        AWSEnvironment
"""

class BaseConfig:

    SECRET_KEY = os.environ.get("SECRET_KEY", "somekey")

    MPESA_BASE_URI = "https://daraja.com"

    SQLALCHEMY_TRACK_MODIFICATIONS =False


    @staticmethod
    def init_app(app):

        pass


class Development(BaseConfig):

    PASS_KEY = os.environ.get("PASS_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.sqlite"

    @staticmethod
    def init_app(app: Flask):

        app.redis_db = Redis(host="localhost", port=6379)

        app.main_queue = Queue("Main",connection=app.redis_db)

        app.email_queue = Queue("Email",connection=app.redis_db)

        

class TestEnvironment(BaseConfig):

    PASS_KEY = "testing"
    SQLALCHEMY_DATABASE_URI ='sqlite:///testing.sqlite'

    @staticmethod
    def init_app(app):

        pass


class Production(BaseConfig):

    SECRETE_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI ="sqlite:///production.sqlite"

    @staticmethod
    def init_app(app):
        pass

environment_config = {
    "testing":TestEnvironment,
    "development":Development,
    "production": Production,
    "default": Development,
}