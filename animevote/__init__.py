from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from animevote.config import Config

db = SQLAlchemy()  # db initialization
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'

from animevote.route import index, login, logout, register, root, poll, show_results


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.id == 1


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)  # db initialization
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from animevote.models import User, Poll   # admin view initialization
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
    return app
