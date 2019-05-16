from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restful import Api
from animevote.config import app_config
from flask_jwt import JWT

db = SQLAlchemy()  # db initialization
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'

from animevote.route import index, login, logout, register, root, poll, show_results
from animevote.user_api import UserList, UserApi
from animevote.models import User


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.username == 'admin'


jwt = JWT(None, User.authenticate, User.identity)


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)  # db initialization
    migrate.init_app(app, db)
    login_manager.init_app(app)
    api = Api(app)
    jwt.init_app(app)

    from animevote.models import User, Poll  # admin view initialization
    admin = Admin(app, template_mode='bootstrap3')
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Poll, db.session))

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
    app.add_url_rule('/root', 'root', root)
    app.add_url_rule('/poll', 'poll', poll)
    app.add_url_rule('/results', 'results', show_results)

    api.add_resource(UserList, "/users")
    api.add_resource(UserApi, "/user/<string:username>")
    return app
