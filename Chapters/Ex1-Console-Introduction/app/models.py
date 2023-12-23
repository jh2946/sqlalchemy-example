from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70))
    email = db.Column(db.String(320))

db.create_all()
