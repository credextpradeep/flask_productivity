from flask import Flask,redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config")



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.login_view = 'auth.signin'
login_manager.init_app(app)
# from config import config
# from app.users.models import User
from app.loginAccount.controllers import second as loginAccount_module
from app.home.controllers import second as home_module
from app.auth.controllers import second as auth_module
from app.settings.controllers import second as config_module
from app.users.controllers import second as user_module


app.register_blueprint(loginAccount_module, url_prefix="/login_account")
app.register_blueprint(home_module)
app.register_blueprint(auth_module)
app.register_blueprint(config_module)
app.register_blueprint(user_module)

@app.route('/')
def hello_world():
    return "<h1>Test</h1>"


# @app.route('/test')
# def test():
#     return render_template("new.html")
# @app.route('/<name>') 
# def user(name):
#   return f"Hello {name}"

# @app.route("/admin")
# def admin():
#   return redirect(url_for("user",name="admin!"))