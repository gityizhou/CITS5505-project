from flask import render_template


def index():
    posts = "test"
    return render_template('index.html', posts=posts)