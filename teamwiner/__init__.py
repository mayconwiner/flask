from flask import Flask , render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SECRET_KEY'] = 'ee23664e6e55f0d81d5f553ee19afe09'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dti.db'

db = SQLAlchemy(app)

from teamwiner import routes