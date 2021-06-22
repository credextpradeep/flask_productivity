from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from app.loginAccount.models import User

class UpdateUser(FlaskForm):
    
    username        = StringField('Username:',render_kw={'readonly':True})
    firstname       = StringField('First Name:', 
                        [DataRequired("First name cannot be empty")],
                        render_kw={"placeholder": "First Name", 'required':True})
    lastname        = StringField('Last Name:', 
                        [DataRequired("Last name cannot be empty")],
                        render_kw={"placeholder": "Last Name", 'required':True})
    account_type    = SelectField('Account Type', coerce=int)
    email           = StringField('Email:',
                        [Email(),
                        DataRequired("Email address cannot be empty"), ],
                        render_kw={"placeholder": "Last Name", 'required':True})
    submit          = SubmitField("Update User")

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
    
    def validate_on_submit(self):
        """

        :rtype: bool
        """
        if not FlaskForm.validate_on_submit(self):
            return False
        return True

class Registrationform(FlaskForm):
  username = StringField('Username:', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
  email = StringField('Email:', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email", 'required':True})
  firstname = StringField('Firstname:', validators=[DataRequired()],render_kw={"placeholder": "First Name"})
  lastname = StringField('Lastname:', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
  account_type = SelectField('Account Type:', coerce=int)
  password = PasswordField('Password:', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "******"})
  confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), Length(min=6), EqualTo('password',message="Passwords must match")], render_kw={"placeholder": "******"})

  submit = SubmitField('Create User')

  def __init__(self, *args, **kwargs):
    FlaskForm.__init__(self, *args, **kwargs)

  def validate_on_submit(self):

    if not FlaskForm.validate_on_submit(self):
      return False

    email = User.query.filter_by(
        email=self.email.data.lower()).first()
    username = User.query.filter_by(
        username=self.username.data.lower()).first()
    if username:
        self.username.errors.append("This username is not available")
        return False
    if email:
        self.email.errors.append("This email is not avaiable")
        return False
    return True
