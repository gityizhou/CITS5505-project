from flask import render_template


def index():
    posts = "test"
    return render_template('index.html', posts=posts)


def login():
    return render_template('login.html')