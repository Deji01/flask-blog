from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5b806d48520009b4d70cb850dc6cdf1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db= SQLAlchemy(app)

from flaskblog import routes