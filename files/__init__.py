from flask import Flask
from files.config import Config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(configClass = Config):
    app = Flask(__name__)
    app.config.from_object(configClass)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app