from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from animevote.models import User


class LoginForm(FlaskForm):
    class Meta:
        csrf = False     # csrf error
    username = StringField("Username", validators=[DataRequired()])  # check
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Password Repeat", validators=[DataRequired(), EqualTo('password')])  # check password equal
    submit = SubmitField('Register')

    def validate_username(self, username):          # check user duplicate
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('please use different username')

    def validate_email(self, email):          # check mail duplicate
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('please use different email address')