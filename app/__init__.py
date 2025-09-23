from flask import Flask
from flask_migrate import Migrate

from config import Config
from app.api import register_blueprints
from app.extensions import db, bcrypt, jwt

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    register_blueprints(app)

    return app
