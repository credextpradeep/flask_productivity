from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

from app.loginAccount.models import User

class RegisterUserBasicInformation(FlaskForm):
    
    username        = StringField('Username', 
                                [DataRequired("Username cannot be empty")],
                                render_kw={"placeholder": "Username", 'class':"form-control", 'required':True})

    firstname       = StringField('First Name', 
                                [DataRequired("First name cannot be empty")],
                                render_kw={"placeholder": "First Name", 'required':True, 'class':"form-control"})

    lastname        = StringField('Last Name', 
                                [DataRequired("Last name cannot be empty")],
                                render_kw={"placeholder": "Last Name", 'required':True, 'class':"form-control"})

    email           = StringField('Email',
                                [Email(message="Not a valid email"),
                                DataRequired("Email address cannot be empty"), ],
                                render_kw={"type": "email", "placeholder": "Email", 'required':True, 'class':"form-control"})
    
    status          = SelectField('Status',
                                coerce=int,
                                render_kw={'class':"form-control"})


    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
    
    def validate_on_submit(self):
        """
        :rtype: bool
        """
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


class UpdateBasicInformation(FlaskForm):
    
    username        = StringField('Username', 
                        render_kw={'readonly': True, 'required':True, 'class':"form-control-plaintext"})
    firstname       = StringField('First Name', 
                        [DataRequired("First name cannot be empty")],
                        render_kw={"placeholder": "First Name", 'required':True, 'class':"form-control"})
    lastname        = StringField('Last Name', 
                        [DataRequired("Last name cannot be empty")],
                        render_kw={"placeholder": "Last Name", 'required':True, 'class':"form-control"})
    email           = StringField('Email',
                        [Email(message="Not a valid email"),
                        DataRequired("Email address cannot be empty"), ],
                        render_kw={'required':True, 'class':"form-control"})
    status          = SelectField('Status', coerce=str, render_kw={'class':"form-control"})
    submit          = SubmitField("Update User Profile")

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
    
    def validate_on_submit(self):
        """

        :rtype: bool
        """
        if not FlaskForm.validate_on_submit(self):
            return False
        return True