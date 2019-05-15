from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required

from animevote import db
from animevote.forms import LoginForm, RegisterForm
from animevote.models import User, Poll


@login_required
def index():
    posts = [
        {
            'author': {'username': 'test1'},
            'body': "hi I'm test1"
        },
        {
            'author': {'username': 'test2'},
            'body': "hi I'm test2"
        },

    ]
    return render_template('index.html', posts=posts)


def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)


def logout():
    logout_user()
    return redirect(url_for('login'))


def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for signing up. Please login.')
        return redirect((url_for('index')))
    return render_template('register.html', title='Registration', form=form)


filename = 'data.txt'


def getpoll():
    question = Poll.query.filter_by(id=1).first().theme
    fields = Poll.query.filter_by(id=1).first().field
    fieldsarr = fields.split(',')
    poll_data = {
        'question': question,
        'fields': fieldsarr
    }
    return poll_data


@login_required
def root():
    return render_template('poll.html', data=getpoll())


@login_required
def poll():
    vote = request.args.get('field')
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()
    return render_template('thankyou.html', data=getpoll())


def show_results():
    votes = {}
    for f in getpoll()['fields']:
        votes[f] = 0
    f = open(filename, 'r')
    votesum = 0
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1
        votesum += 1
    return render_template('results.html', data=getpoll(), votes=votes, votesum=votesum)
