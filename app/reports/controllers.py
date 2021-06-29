from os import times
from typing import Dict
from app.loginAccount.models import User, UserGroup
from flask import Blueprint, config, request, render_template, Flask
from flask.templating import render_template
from app.reports.models import DayWiseStats, db
from .models import usege_report
from datetime import datetime, time, timedelta, date
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

second = Blueprint('usege_reports', __name__,template_folder="templates", url_prefix='/usege_reports')

@second.route('/', methods=["GET","POST"])
def usege_reports():
    all_usege_report = usege_report.query.all() 
    start_date = date.today()
    end_date = date.today()-timedelta(days=7)
    start_time = time(23, 8, 15)
    end_time = time
    # duration = request.args.get(start_time, end_time)
    # seconds = duration
    # days    = divmod(seconds, 86400)       
    # hours   = divmod(days[1], 3600)               
    # minutes = divmod(hours[1], 60)                
    # seconds = divmod(minutes[1], 1)               
    # print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))
    # date_range = request.args.get(start_date, end_date)
    print(start_time, end_time)

    # date_range = request.post_vars['date_range']
    # post_var = request.post_vars['date_range'].split(" - ")
    # start_date = post_var[0]
    # end_date   = post_var[1]
    # print(start_date,end_date)
    # usage = usageReport(getCorrectFormatDate(post_var[0]), getCorrectFormatDate(post_var[1]))
    print(all_usege_report)
    return render_template('usege_reports/usege_reports.html',all_usege_report=all_usege_report, start_date=start_date, end_date=end_date)

def yesterdaysDate():
    x = datetime.now() - timedelta(days = 1)
    return x.strftime("%Y-%m-%d") 

def getYesterdayLoginCount():
    return DayWiseStats.query.filter_by(date=yesterdaysDate()).count()

