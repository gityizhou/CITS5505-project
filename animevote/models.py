from animevote import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'id={}, username={}, email={}, password_hash={}'.format(
            self.id, self.username, self.email, self.password_hash
        )


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(140))
    field = db.Column(db.String(400))

    def __repr__(self):
        return "id={},theme={}, field={}".format(
            self.id, self.theme, self.field
        )