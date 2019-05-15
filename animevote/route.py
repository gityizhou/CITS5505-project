from flask import render_template, redirect, url_for, flash
from animevote.forms import LoginForm
from animevote.models import User, Poll


def index():
    posts = "test"
    return render_template('index.html', posts=posts)


def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)
