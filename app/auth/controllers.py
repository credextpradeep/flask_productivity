from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash

from app import db
from app.loginAccount.models import User
from .forms import SigninForm
second = Blueprint('auth', __name__, url_prefix='/auth')


@second.route('/', methods=['GET', 'POST'])
def signin():
    # If sign in form is submitted
    if not current_user.is_anonymous:
        return redirect(url_for('home.index'))

    form = SigninForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            user = User.query.filter_by(username=form.username.data).first()
            
            if user and check_password_hash(user.password, form.password.data):
                session['username'] = user.username
                session['email'] = user.email
                flash('Welcome %s' % user.username, 'success')
                login_user(user)
                return redirect(url_for('home.index'))
            flash('Wrong username or password', 'error')
            
    return render_template("/auth/signin.html", form=form)


@second.route('/<id>', methods=['GET'])
def get_user(id):
    result = User.query.get(id)
    return result.username


@second.route('/signout', methods=['GET'])
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.signin'))