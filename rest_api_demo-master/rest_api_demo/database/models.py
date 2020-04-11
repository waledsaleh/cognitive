# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api_demo.database import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(50))

    def __init__(self, name):
        self.pet_name = name

    def __repr__(self):
        return '<Pet %r>' % self.pet_name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bid_amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('bid', lazy='dynamic'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    pet = db.relationship('Pet', backref=db.backref('bid', lazy='dynamic'))

    def __init__(self, bid_amount,user,pet):
        self.bid_amount = bid_amount
        self.user = user
        self.pet = pet
    def __repr__(self):
        return '<Bid %r>' % self.bid_amount