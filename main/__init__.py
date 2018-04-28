from controllers import main_bp
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

main = Flask(__name__)
main.config.from_object("config")

db = SQLAlchemy(main)

def init_db(sql_string=None):
    if sql_string:
        # This is done for Flask SQLAlchemy
        main.config["SQLALCHEMY_DATABASE_URI"] = main.config["SQLALCHEMY_TEST_DATABASE_URI"]

    db.create_all()
    db.session.commit()

def init_blueprints():
    main.register_blueprint(main_bp)
    from api import main_api
    main.register_blueprint(main_api)

login_manager = LoginManager()
login_manager.init_app(main)
login_manager.login_view = "controllers.login"

@login_manager.user_loader
def load_user(userid):
    from models import User
    return User.query.filter_by(id=userid).first()
