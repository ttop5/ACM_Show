import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager
from config import config


app = Flask(__name__)
db = MongoEngine()
login_manager = LoginManager()


with app.app_context():
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import UserModel

    @login_manager.user_loader
    def load_user(id):
        return UserModel.objects(id=id).first()

    from .views import bp_auth

    app.register_blueprint(
        bp_auth,
        url_prefix='/auth'
    )

from app import views, models


