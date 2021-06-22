from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired

from app.settings.models import AllowedApps

class GlobalConfigurationForm(FlaskForm):

  CS1 = IntegerField('Remote Auth Fail Duration',
                    [DataRequired('Remote Auth Fail Duration cannot be empty')],
                    render_kw={'type':'number','required':True})
  
  CS2 = IntegerField('Remote Auth Fail Attempts',
                    [DataRequired('Remote Auth Fail Attempts cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS3 = IntegerField('Remote Auth Step Time',
                    [DataRequired('Remote Auth Step Time cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS4 = BooleanField('Local Auth Enable')

  CS5 = IntegerField('Local Auth Duration',
                    [DataRequired('Local Auth Duration cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS6 = IntegerField('Local Auth Step Time',
                    [DataRequired('Local Auth Step Time cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS7 = IntegerField('Local Auth Fail Attempts',
                    [DataRequired('Local Auth Fail Attempts cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS8 = IntegerField('Local Auth Threshold',
                    [DataRequired('Local Auth Step Time cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS9 = IntegerField('Log Level',
                    [DataRequired('Local Auth Step Time cannot be empty')],
                    render_kw={'type':'number','required':True})

  CS10 = BooleanField('Eye Enable')

  CS11 = BooleanField('Allow Multi Face')

  CS12 = BooleanField('Detect Multi Monitor')

  CS13 = BooleanField('Biometrical Mode')

  CS14 = BooleanField('AI Enable')

 

  submit = SubmitField("Update Config")

def getConfigurationForm(conf) :
        return GlobalConfigurationForm(
                        CS1  = int(conf["CS1"]),
                        CS2 = int(conf["CS2"]),
                        CS3 = int(conf["CS3"]),
                        CS4 = int(conf["CS4"]),
                        CS5 = int(conf["CS5"]),
                        CS6 = int(conf["CS6"]),
                        CS7 = int(conf["CS7"]),
                        CS8 = int(conf["CS8"]),
                        CS9 = int(conf["CS9"]),
                        CS10 = int(conf["CS10"]),
                        CS11 = int(conf["CS11"]),
                        CS12 = int(conf["CS12"]),
                        CS13 = int(conf["CS13"]),
                        CS14 = int(conf["CS14"]),
                )

class AllowedAppsForm(FlaskForm):
  application_title = StringField('Application Title',
                      [DataRequired("Application title can not be empty")],
                      render_kw={"placeholder":"Application Title",'class':'form-control','required':True})

  application_tag = StringField('Application Tag',
                    [DataRequired("Application tag can not be empty")], 
                    render_kw={"placeholder":"Application Tag",'class':'form-control','required':True})
  
  submit          = SubmitField("Submit")

  def __init__(self, *args, **kwargs):
    FlaskForm.__init__(self, *args, **kwargs)
    
  def validate_on_submit(self):
    if not FlaskForm.validate_on_submit(self):
      return False

    application_title = AllowedApps.query.filter_by(
        application_title=self.application_title.data.lower()).first()
    application_tag = AllowedApps.query.filter_by(
        application_tag=self.application_tag.data.lower()).first()
    if application_tag:
        self.application_tag.errors.append("This application tag is not available")
        return False
    if application_title:
        self.application_title.errors.append("This application title is not avaiable")
        return False
    return True

class UpdateAppForm(FlaskForm):
  application_title = StringField('Application Title',
                      [DataRequired("Application title can not be empty")],
                      render_kw={"placeholder":"Application Title",'class':'form-control','required':True})

  application_tag = StringField('Application Tag',
                    [DataRequired("Application tag can not be empty")], 
                    render_kw={"placeholder":"Application Tag",'class':'form-control','required':True})
  
  submit          = SubmitField("Submit")

  def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
    
  def validate_on_submit(self):
    """

    :rtype: bool
    """
    if not FlaskForm.validate_on_submit(self):
      return False
    return True