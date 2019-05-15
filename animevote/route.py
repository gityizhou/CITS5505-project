from flask import render_template
from animevote.forms import LoginForm


def index():
    posts = "test"
    return render_template('index.html', posts=posts)


def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)
