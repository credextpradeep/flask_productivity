from app import db

class DayWiseStats(db.Model):

  __tablename_ = 'day_wise_stats'

  id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username            = db.Column(db.String(10), nullable=False, index=True)
  date                = db.Column(db.Date, nullable=False)
  no_of_sessions      = db.Column(db.Integer, nullable=False, default=0)
  total_login_minutes = db.Column(db.Integer, nullable=False)
  created_at          = db.Column(db.DateTime, default=db.func.now())