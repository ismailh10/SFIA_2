from application import routes

from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:qaconsulting@35.246.121.150/flaskapp"
app.config['SECRET_KEY'] =  str(os.getenv('SECRET_KEY'))

db = SQLAlchemy(app)




