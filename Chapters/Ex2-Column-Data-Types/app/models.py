from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(320), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String)
    balance = db.Column(db.Numeric, nullable=False)
    vip = db.Column(db.Boolean, nullable=False)
    signUpDate = db.Column(db.DateTime, nullable=False)

db.create_all()
