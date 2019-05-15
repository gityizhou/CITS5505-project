from animevote import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'id={}, username={}, email={}, password_hash={}'.format(
            self.id, self.username, self.email, self.password_hash
        )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader  # 用于记住用户
def load_user(id):
    return User.query.get(int(id))


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(140))
    field = db.Column(db.String(400))

    def __repr__(self):
        return "id={},theme={}, field={}".format(
            self.id, self.theme, self.field
        )
