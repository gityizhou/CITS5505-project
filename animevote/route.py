from flask import render_template, redirect
from animevote.forms import LoginForm


def index():
    posts = "test"
    return render_template('index.html', posts=posts)


def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect("/")

    return render_template('login.html', title="Sign In", form=form)
