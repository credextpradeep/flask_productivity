from flask import Blueprint, request
from app.loginAccount.models import User
from app.settings.models import GlobalConfiguration
import os
import json


second = Blueprint('common', __name__, url_prefix='/common')

@second.route('/check_username', methods=['POST'])
def check_username():
    print(request.json['username'])
    # username = db(db.user.username == request.post_vars['username']).select(db.user.username).first()
    # print username['username']
    user = User.query.filter_by(username=request.json['username']).first()
    
    if user:
        # print "username already exist"
        return json.dumps({'statusCode': True})
    else:
        return json.dumps({'statusCode': False})

# @mod.route('/get_glob_config')
def get_glob_config():
    glb_settings = GlobalConfiguration.query.all()
    glb_settings_dict = {}
    for setting in glb_settings:
        glb_settings_dict[setting.key] = setting.value
    return glb_settings_dict


# returns default value , choices
def getUserStatus():
    return 1, [('F', "Activate"), ('T', "Deactivate")]