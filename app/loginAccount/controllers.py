from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import Registrationform, UpdateUser
from app import db
from .models import User, UserGroup
from flask_login import login_required
second = Blueprint("login_account",__name__,template_folder="templates",url_prefix='/login_account')



@second.route('/', methods=['GET'])
def index():
    users = User.query.filter(User.group_id == UserGroup.query.with_entities(UserGroup.id).filter_by(role="Admin")).all()
    user_group = UserGroup.query.all()
    group_list = {group.id: group.role for group in user_group}
    return render_template('users/manage_login_acc.html', users=users, group=group_list)
    


@second.route("/add", methods=['GET','POST'])
@login_required
def register_user():
    form = Registrationform()

    user_group = UserGroup.query.with_entities(UserGroup.id, UserGroup.role).all()
    # print(user_group)
    account_types = [(item.id, item.role) for item in user_group]
    form.account_type.choices = account_types
    # form.account_type.choices = user_group
    form.account_type.default = 1

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html', form=form)

        user = User(username=form.username.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    group_id=form.account_type.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User registered successfully for {form.username.data}', 'success')
        return redirect(url_for('login_account.index'))

    return render_template('users/register.html', form=form)


@second.route('/<username>', methods=['GET', 'POST'])
@login_required
def edit_user(username):
    user = User.query.filter_by(username=username).first()
    user_group = UserGroup.query.with_entities(UserGroup.id, UserGroup.role).all()
    
    form = UpdateUser(account_type=user.group_id)
    account_types = [(item.id, item.role) for item in user_group]
    form.account_type.choices = account_types


    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/edit-user.html', form=form, user=user, group=user_group)

        user.email      = form.email.data
        user.firstname  = form.firstname.data
        user.lastname   = form.lastname.data
        user.group_id   = form.account_type.data
        db.session.commit()
        flash("Information has been updated", "success")
    return render_template('users/edit-user.html', form=form, user=user, group=user_group)
