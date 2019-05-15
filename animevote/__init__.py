from flask import Flask
from animevote.route import index


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/index', 'index', index)
    return app

