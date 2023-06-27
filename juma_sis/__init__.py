from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '54fdc2aa9e6a6077e9925a3a5ee175dd7004a6b0a4405a427fb90d5944983fae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///juma_database.db'

database = SQLAlchemy(app)


from juma_sis import routes