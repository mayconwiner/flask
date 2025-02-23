from flask import Flask , render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)



app.config['SECRET_KEY'] = 'ee23664e6e55f0d81d5f553ee19afe09'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dti.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar esta página'
login_manager.login_message_category = 'alert-info'

from teamwiner import routes