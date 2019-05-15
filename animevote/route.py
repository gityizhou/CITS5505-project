from flask import render_template, redirect, url_for
from animevote.forms import LoginForm
from animevote.models import User


def index():
    posts = "test"
    return render_template('index.html', posts=posts)


def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('login.html', title="Sign In", form=form)
