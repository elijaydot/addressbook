from app import db


class ContactBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(length=100))
    last_name = db.Column(db.Text(length=100))
    phone_number = db.Column(db.Text(length=15))
    email = db.Column(db.Text(length=200))
    complete = db.Column(db.Boolean)
