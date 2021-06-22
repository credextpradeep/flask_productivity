import os
import shutil
from datetime import datetime
from flask_login import login_required
from flask import Blueprint, render_template, url_for, request, flash, redirect

from app.users.forms import RegisterUserBasicInformation, UpdateBasicInformation

from app.loginAccount.models import User, UserConfiguration, Organisation, UserGroup, UserMembership

from app.settings.models import GlobalConfiguration
from app.settings.forms import getConfigurationForm
from app.settings.controllers import getGlobalConfiguration, getGlobalConfForUserConf

from app.modules.controllers import getUserStatus

from app import db
import json


second = Blueprint('users', __name__, url_prefix='/users')

@second.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    global_conf = GlobalConfiguration.query.all()
    conf = {item.key: item.value  for item in global_conf}
    globalConfForm = getConfigurationForm(conf)

    basicInfoForm = RegisterUserBasicInformation()
    defaultStatus, statusChoices = getUserStatus()
    basicInfoForm.status.choices = statusChoices
    basicInfoForm.status.default = defaultStatus
    
    if request.method == "POST":
        if not globalConfForm.validate_on_submit():
            return render_template('user/add_user.html', form = globalConfForm, basicInfoForm = basicInfoForm)       

        if not basicInfoForm.validate_on_submit():
            return render_template('user/add_user.html', form = globalConfForm, basicInfoForm = basicInfoForm)
        status = 'F'
        if basicInfoForm.status.data == 'T':
          status = 'T'
        username = basicInfoForm.username.data

        credext = Organisation.query.filter_by(name='Credext').first()
        group = UserGroup.query.filter_by(role='Admin').first()
        user = User(firstname = basicInfoForm.firstname.data, 
                    lastname  = basicInfoForm.lastname.data,
                    email     = basicInfoForm.email.data,
                    username  = username, 
                    group_id  = group.id, 
                    password  = 'credext', 
                    organisation_id = credext.id,
                    approved  = 'T')
        user.block_user = status
        db.session.add(user)
        db.session.commit()
        configuration = json.dumps(updateConfFromFormData(globalConfForm))
        if user:
            user_settings = UserConfiguration(user_id=user.id, configuration=configuration)      
            db.session.add(user_settings)
            db.session.commit()

            flash("User registered successfully", "success")
            return redirect(url_for("users.all_user"))
        
    return render_template('user/add_user.html', form = globalConfForm, basicInfoForm = basicInfoForm)


@second.route('/all_user', methods=['GET'])
@login_required
def all_user():
    all_users = getAllUsers()
    # for user in all_users:
    #     print(user.firstname)
    return render_template('user/all_user.html', all_users=all_users)


def getAllUsers():
    return User.query.filter_by(group_id = UserGroup.query.with_entities(UserGroup.id).filter_by(role="Admin"), approved='T').all()


def getUsersCount():
    userCount = User.query.filter_by(group_id = UserGroup.query.with_entities(UserGroup.id).filter_by(role="Admin")).count()
    return userCount
    
def getTimeStamp():
    """Get time stamp that can be used in file names."""
    stamp = datetime.now()
    return stamp.strftime('%Y%m%d_%H%M%S%f')

@second.route('/<username>', methods=['GET', 'POST'])
@login_required
def edit_user(username):
    user = User.query.filter_by(username=username).first()
    
    form = UpdateBasicInformation()
    defaultStatus, statusChoices = getUserStatus()
    form.status.choices = statusChoices
    form.status.default = defaultStatus

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('user/update-user.html', form=form, user=user)

        user.email      = form.email.data
        user.firstname  = form.firstname.data
        user.lastname   = form.lastname.data
        user.block_user = form.status.data
        db.session.commit()
        flash("Information has been updated", "success")
    return render_template('user/update-user.html', form=form, user=user)

@second.route('/del_user/<user_id>', methods=['GET','POST'])
@login_required
def del_user(user_id):
    user = User.query.filter_by(id= user_id).first()
    username = user.username
    UserConfiguration.query.filter_by(user_id=user.id).delete()
    UserMembership.query.filter_by(user_id = user.id).delete()
    user = User.query.filter_by(username=username).delete()
    db.session.commit()

    if user:
        flash("Successfully deleted "+ username, "success")
    return redirect(url_for('users.all_user'))


def getUserConfiguration(user_configuration):

    configuration = eval(user_configuration)
    conf = {}

    conf["CS1"] = int(configuration["CS1"])
    conf["CS2"] = int(configuration["CS2"])
    conf["CS3"] = int(configuration["CS3"])
    if configuration["CS4"] == 1:
        conf["CS4"] = True
    else:
        conf["CS4"] = False
    conf["CS5"] = int(configuration["CS5"])
    conf["CS6"] = int(configuration["CS6"])
    conf["CS7"] = int(configuration["CS7"])
    conf["CS8"] = int(configuration["CS8"])
    conf["CS9"] = int(configuration["CS9"])
    if configuration["CS10"] == 1:
        conf["CS10"] = True
    else:
        conf["CS10"] = False
    if configuration["CS11"] == 1:
        conf["CS11"] = True
    else:
        conf["CS11"] = False
    if configuration["CS12"] == 1:
        conf["CS12"] = True
    else:
        conf["CS12"] = False

    if configuration["CS13"] == 1:
        conf["CS13"] = True
    else:
        conf["CS13"] = False

    if configuration["CS14"] == 1:
        conf["CS14"] = True
    else:
        conf["CS14"] = False
        
    return conf


def createJSONforUserConfiguration(configuration):
    return json.dumps(configuration)


# this function creates data for user_configuration table 
def setUserConfiguration(request):
    conf = {}
    conf["CS1"]     = int(request.get("CS1"))
    conf["CS2"]     = int(request.get("CS2"))
    conf["CS3"]     = int(request.get("CS3"))
    if request.get("CS4"):
        conf["CS4"] = 1
    else:
        conf["CS4"] = 0
    conf["CS4"]     = int(request.get("CS4"))
    conf["CS5"]     = int(request.get("CS5"))
    conf["CS6"]     = int(request.get("CS6"))
    conf["CS7"]     = int(request.get("CS7"))
    conf["CS8"]     = int(request.get("CS8"))
    conf["CS9"]     = int(request.get("CS9"))
    if request.get("CS10"):
        conf["CS10"] = 1
    else:
        conf["CS10"] = 0
    if request.get("CS11"):
        conf["CS11"] = 1
    else:
        conf["CS11"] = 0
    if request.get("CS12"):
        conf["CS12"] = 1
    else:
        conf["CS12"] = 0
    
    if request.get("CS13"):
        conf["CS13"] = 1
    else:
        conf["CS13"] = 0
    
    if request.get("CS14"):
        conf["CS14"] = 1
    else:
        conf["CS14"] = 0

    return json.dumps(conf)



def updateConfFromFormData(form):
    conf = {}

    conf["CS1"] = int(form.CS1.data)
    conf["CS2"] = int(form.CS2.data)
    conf["CS3"] = int(form.CS3.data)
    conf["CS4"] = int(form.CS4.data)
    conf["CS5"] = int(form.CS5.data)
    conf["CS6"] = int(form.CS6.data)
    conf["CS7"] = int(form.CS7.data)
    conf["CS8"] = int(form.CS8.data)
    conf["CS9"] = int(form.CS9.data)
    conf["CS10"] = int(form.CS10.data)
    conf["CS11"] = int(form.CS11.data)
    conf["CS12"] = int(form.CS12.data)
    conf["CS13"] = int(form.CS13.data)
    conf["CS14"] = int(form.CS14.data)

    return conf
    
