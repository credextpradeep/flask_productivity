from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.users.controllers import getUsersCount, getAllUsers
from app.settings.controllers import getAllApplicationsCount
from app.reports.controllers import getYesterdayLoginCount
second = Blueprint("home",__name__,template_folder="templates",url_prefix='/home')


@second.route("/") 
def index():
    users = {user.username:{"id": user.id, "name":user.firstname+" "+user.lastname} for user in getAllUsers()}
    stats = {}
    stats["usercount"] = getUsersCount()
    stats['appcount'] = getAllApplicationsCount()
    stats["yesterdayLoginCount"] = getYesterdayLoginCount()
    # stats["getYesterdaysBestPerformers"] = getYesterdaysBestPerformers()
    # stats["getYesterdaysLoginHrs"] = getYesterdaysLoginHrs().time
    return render_template('home/index.html', users=users, stats=stats)