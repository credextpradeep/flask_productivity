# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from app.loginAccount.models import User


class SigninForm(FlaskForm):
    """ login form"""

    username = StringField(
        'Username',
        [DataRequired(message='Must provide a User Name.'), ], )
    password = PasswordField(
        'Password',
        [DataRequired(message='Must provide a password.'), ], )
    remember = BooleanField()

    submit = SubmitField('Submit')





