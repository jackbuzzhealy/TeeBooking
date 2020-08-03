from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)


from application import routes
