from flask import Flask, has_app_context
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

app = Flask(__name__)
if not has_app_context():
    app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
