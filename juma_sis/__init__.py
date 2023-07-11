from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '54fdc2aa9e6a6077e9925a3a5ee175dd7004a6b0a4405a427fb90d5944983fae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///juma_database.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça Login para continuar'
login_manager.login_message_category = 'alert-info'

from juma_sis import routes