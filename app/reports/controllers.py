from flask import Blueprint, request
from app.reports.models import DayWiseStats
from datetime import datetime, timedelta, date

second = Blueprint('reports', __name__, url_prefix='/reports')

def yesterdaysDate():
    x = datetime.now() - timedelta(days = 1)
    return x.strftime("%Y-%m-%d")

def getYesterdayLoginCount():
    return DayWiseStats.query.filter_by(date=yesterdaysDate()).count()