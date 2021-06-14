from app import db,login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)
    
class User(db.Model, UserMixin):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True,autoincrement=True)
  username = db.Column(db.String(64),nullable=False,unique=True)
  firstname = db.Column(db.String(128), nullable=False)
  group_id = db.Column(db.Integer, db.ForeignKey('user_group.id'))
  organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id'))
  lastname = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), nullable=False,
  unique=True)
  password = db.Column(db.String(154), nullable=False)
  user_membership     = db.relationship('UserMembership')
  configuration       = db.relationship('UserConfiguration', foreign_keys='UserConfiguration.user_id')
  created_at          = db.Column(db.DateTime, default=db.func.now())
  updated_at          = db.Column(db.DateTime, onupdate=db.func.now())
  approved            = db.Column(db.String(1), nullable=True, default='T')
  registration_id     = db.Column(db.String(50), nullable=True)
  registration_key    = db.Column(db.String(512), nullable=True)
  reset_password_key  = db.Column(db.String(512), nullable=True)
  block_user          = db.Column(db.String(1), nullable=False, default='F')

  def __init__(self,username,firstname,lastname,group_id,email,password, organisation_id,approved='T'):
    self.username = username
    self.firstname = firstname
    self.lastname = lastname
    self.group_id = group_id
    self.email = email
    self.set_password(password)
    self.organisation_id = organisation_id
    self.approved = approved

  def __repr__(self):
        return '<User %s>' % self.username

  def set_password(self, password):
        self.password = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password, password)

  @classmethod
  def get(cls, user_id):
    try:
      return User.query.filter_by(id=user_id).one()
    except NoResultFound:
      return None
    

class UserGroup(db.Model):
    __tablename__ = 'user_group'

    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role            = db.Column(db.String(50), nullable=False, unique=True)
    description     = db.Column(db.String(255), nullable=True)
    user_membership = db.relationship("UserMembership")
    created_at      = db.Column(db.DateTime, default=db.func.now())
    updated_at      = db.Column(db.DateTime, onupdate=db.func.now())

class Organisation(db.Model):
    __tablename__ = 'organisations'
    
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name            = db.Column(db.String(100), nullable=False)
    details         = db.Column(db.String(255), nullable=True)
    public_ip       = db.Column(db.String(15), nullable=True)
    admin_mailid    = db.Column(db.String(50), nullable=True)
    users           = db.relationship("User")
    created_at      = db.Column(db.DateTime, default=db.func.now())
    updated_at      = db.Column(db.DateTime, onupdate=db.func.now())


class UserMembership(db.Model):
    __tablename__ = 'user_membership'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    group_id    = db.Column(db.Integer, db.ForeignKey('user_group.id'))
    
    created_at  = db.Column(db.DateTime, default=db.func.now())
    updated_at  = db.Column(db.DateTime, onupdate=db.func.now())

class UserConfiguration(db.Model):
    __tablename__ = 'user_configuration'

    id                      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id                 = db.Column(db.Integer, db.ForeignKey('user.id'))
    configuration           = db.Column(db.String(1024), nullable=False)
    created_at              = db.Column(db.DateTime, default=db.func.now())
    updated_at              = db.Column(db.DateTime, onupdate=db.func.now())