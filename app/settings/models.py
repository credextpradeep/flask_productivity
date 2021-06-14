from app import db

class GlobalConfiguration(db.Model):
    __tablename__ = 'global_configuration'
    
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key         = db.Column(db.String(100), nullable=False, unique=True)
    value       = db.Column(db.String(100), nullable=False)

    created_at  = db.Column(db.DateTime, default=db.func.now())
    updated_at  = db.Column(db.DateTime, onupdate=db.func.now())