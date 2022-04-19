import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    config_name = os.getenv('FLASK_ENV')

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_name])

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from .controllers import Controllers
    from .models import Models
    Controllers.init_app(app)
    Models.init_app(app)

    @app.route('/ping')
    def ping():
        return 'pong!'

    return app
