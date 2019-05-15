from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from animevote.route import index, login


db = SQLAlchemy()    # db initialization
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:animevote.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
    db.init_app(app)     # db initialization
    migrate.init_app(app, db)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    return app

