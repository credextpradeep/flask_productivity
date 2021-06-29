from datetime import time
from sqlalchemy.orm import column_property
from app import db

class DayWiseStats(db.Model):

  __tablename_ = 'day_wise_stats'

  id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username            = db.Column(db.String(10), nullable=False, index=True)
  date                = db.Column(db.Date, nullable=False)
  no_of_sessions      = db.Column(db.Integer, nullable=False, default=0)
  total_login_minutes = db.Column(db.Integer, nullable=False)
  created_at          = db.Column(db.DateTime, default=db.func.now())


class usege_report(db.Model):

  __tablname_ = 'usege_reports'
  id                        = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username                  = db.Column(db.String(10), nullable=False, index=True)
  full_name                 = db.Column(db.String(128), nullable=False)
  number_of_days            = db.Column(db.Integer, nullable=False)
  Gross_Login_Time          = db.Column(db.Time, nullable=False, default=0)
  Effective_Working_Hrs     = db.Column(db.String(50), nullable=False)
  Idle_Hrs                  = db.Column(db.Time, default=db.func.now())
  # idle_hours_percen         = db.column(db.time, default = db.func.now())
  No_of_Sessions            = db.Column(db.Integer, nullable=False, default=0)
  idle_hours010             = db.Column(db.String(50), default=db.func.now())
  idle_hours1020            = db.Column(db.String(50), default=db.func.now())
  idle_hours2030            = db.Column(db.String(50), default=db.func.now())
  idle_hours30more          = db.Column(db.String(50), default=db.func.now())
  apps_spent_hrs            = db.Column(db.Time, default=db.func.now())
  l1                        = db.Column(db.String(128), nullable=False)
  l2                        = db.Column(db.String(128), nullable=False)
  l3                        = db.Column(db.String(128), nullable=False)
  l4                        = db.Column(db.String(128), nullable=False)
  l5                        = db.Column(db.String(128), nullable=False)
  l6                        = db.Column(db.String(128), nullable=False)
  l7                        = db.Column(db.String(128), nullable=False)
  l8                        = db.Column(db.String(128), nullable=False)
  l9                        = db.Column(db.String(128), nullable=False)
  
  
       
  	