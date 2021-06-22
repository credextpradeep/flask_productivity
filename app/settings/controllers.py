import time
import os
from flask_login import login_required
from flask import Blueprint, render_template, request, flash, redirect
from flask import current_app, url_for
from sqlalchemy import event
from sqlalchemy.engine import Engine
from app import db
import shutil
from .models import GlobalConfiguration, AllowedApps
from .forms import getConfigurationForm, AllowedAppsForm, UpdateAppForm
from app.loginAccount.models import UserConfiguration
import json

second = Blueprint('settings', __name__, url_prefix='/settings')



@second.route('/global_configuration', methods=['GET', 'POST'])
@login_required
def global_configuration():
    global_conf = GlobalConfiguration.query.all()
    conf = {item.key: item.value  for item in global_conf}
    form = getConfigurationForm(conf)

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('settings/configurations.html', form=form, settings=conf)
        
        for item in global_conf:
            if item.key == "CS1":
                item.value = form.CS1.data
            elif item.key == "CS2":
                item.value = form.CS2.data
            elif item.key == "CS3":
                item.value = form.CS3.data
            elif item.key == "CS4":
                item.value = form.CS4.data
            elif item.key == "CS4":
                item.value = form.CS4.data
            elif item.key == "CS5":
                item.value = form.CS5.data
            elif item.key == "CS6":
                item.value = form.CS6.data
            elif item.key == "CS7":
                item.value = form.CS7.data
            elif item.key == "CS8":
                item.value = form.CS8.data
            elif item.key == "CS9":
                item.value = form.CS9.data
            elif item.key == "CS10":
                item.value = form.CS10.data
            elif item.key == "CS11":
                item.value = form.CS11.data
            elif item.key == "CS12":
                item.value = form.CS12.data
            elif item.key == "CS13":
                item.value = form.CS13.data
            elif item.key == "CS14":
                item.value = form.CS14.data
                        
        db.session.commit()
        
        configuration = json.dumps(getGlobalConfForUserConf())
        UserConfiguration.query.update({UserConfiguration.configuration:configuration})
        db.session.commit()

        flash("Global Configuration updated successfully", 'success')
    return render_template('settings/configurations.html', form=form, settings=conf)


def getGlobalConfiguration():
    
    global_conf = {}
    for item in GlobalConfiguration.query.all():
        if item.key == "CS1":
          global_conf["CS1"] = int(item.value)
        elif item.key == "CS2":
            global_conf["CS2"] = int(item.value)
        elif item.key == "CS3":
            global_conf["CS3"] = int(item.value)
        elif item.key == "CS4":
          if item.value == "1":
            global_conf["CS4"] = True
          else:
            global_conf["CS4"] = False
        elif item.key == "CS5":
            global_conf["CS5"] = float(item.value)
        elif item.key == "CS6":
            global_conf["CS6"] = int(item.value)
        elif item.key == "CS7":
            global_conf["CS7"] = int(item.value)
        elif item.key == "CS8":
            global_conf["CS8"] = int(item.value)
        elif item.key == "CS9":
            global_conf["CS9"] = int(item.value)
        elif item.key == "CS10":
          if item.value == "1":
            global_conf["CS10"] = True
          else:
            global_conf["CS10"] = False
        elif item.key == "CS11":
          if item.value == "1":
            global_conf["CS11"] = True
          else:
            global_conf["CS11"] = False
        elif item.key == "CS12":
          if item.value == "1":
            global_conf["CS12"] = True
          else:
            global_conf["CS12"] = False
        elif item.key == "CS13":
          if item.value == "1":
            global_conf["CS13"] = True
          else:
            global_conf["CS13"] = False
        elif item.key == "CS14":
          if item.value == "1":
            global_conf["CS14"] = True
          else:
            global_conf["CS14"] = False
        
    return global_conf


def getGlobalConfForUserConf():
    global_conf = {}
    for item in GlobalConfiguration.query.all():
        if item.key == "CS1":
            global_conf["CS1"] = int(item.value)
        elif item.key == "CS2":
            global_conf["CS2"] = int(item.value)
        elif item.key == "CS3":
            global_conf["CS3"] = int(item.value)
        elif item.key == "CS4":
          if item.value == "1":
            global_conf["CS4"] = 1
          else:
            global_conf["CS4"] = 0
        elif item.key == "CS5":
            global_conf["CS5"] = float(item.value)
        elif item.key == "CS6":
            global_conf["CS6"] = int(item.value)
        elif item.key == "CS7":
            global_conf["CS7"] = int(item.value)
        elif item.key == "CS8":
            global_conf["CS8"] = int(item.value)
        elif item.key == "CS9":
            global_conf["CS9"] = int(item.value)
        elif item.key == "CS10":
          if item.value == "1":
            global_conf["CS10"] = 1
          else:
            global_conf["CS10"] = 0
        elif item.key == "CS11":
          if item.value == "1":
              global_conf["CS11"] = 1
          else:
              global_conf["CS11"] = 0
        elif item.key == "CS12":
            if item.value == "1":
                global_conf["CS12"] = 1
            else:
                global_conf["CS12"] = 0
        elif item.key == "CS13":
            if item.value == "1":
                global_conf["CS13"] = 1
            else:
                global_conf["CS13"] = 0
        elif item.key == "CS14":
            if item.value == "1":
                global_conf["CS14"] = 1
            else:
                global_conf["CS14"] = 0

    return global_conf



def getAllApplications():
    return AllowedApps.query.all()


def getAllApplicationsCount():
    appCount = AllowedApps.query.count()
    return appCount

@second.route('/allowed_apps', methods=['GET', 'POST'])
@login_required
def addAllowedApps():
    form = AllowedAppsForm()
    allowed_apps = AllowedApps.query.all()

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('settings/allowed_apps.html', form=form)

        app = AllowedApps(application_title=form.application_title.data,
                          application_tag=form.application_tag.data)
        db.session.add(app)
        db.session.commit()
        flash(f'App added successfully', 'success')
    allApps = getAllApplications()

    return render_template('settings/allowed_apps.html', form=form, allApps = allApps)


@second.route('/<id>', methods=['GET', 'POST'])
@login_required
def edit_app(id):
    app = AllowedApps.query.filter_by(id=id).first()
    
    form = UpdateAppForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('settings/edit-app.html', form=form, app=app)

        app.application_tag      = form.application_tag.data
        app.application_title  = form.application_title.data
        db.session.commit()
        flash("Information has been updated", "success")
    return render_template('settings/edit-app.html', form=form, app=app)


@second.route('/del_app/<id>', methods=['GET','POST'])
@login_required
def del_app(id):
    app = AllowedApps.query.filter_by(id= id).first()
    print("*****************",app)
    application_title = app.application_title
    app = AllowedApps.query.filter_by(id=id).delete()
   
    db.session.commit()

    if app:
        flash("Successfully deleted "+ application_title, "success")
    return redirect(url_for('settings.addAllowedApps'))