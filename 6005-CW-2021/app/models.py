import hashlib
import datetime

from flask_sqlalchemy import SQLAlchemy

import app.meta as meta

db = SQLAlchemy(meta.app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image = db.Column(db.Text)
    category = db.Column(db.Text)
    hidden = db.Column(db.Boolean, default=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    level = db.Column(db.Text, default="user")


    def setPassword(self, password):
        #We want to hash the password

        theHash = hashlib.sha512(password.encode()).hexdigest()
        self.password = theHash


    def checkPassword(self, password):
        """Check if the password the user specifies is good"""

        hashed  = hashlib.sha512(password.encode()).hexdigest()
        return hashed == self.password

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    itemId = db.Column(db.Integer, db.ForeignKey('item.id'))
    stars = db.Column(db.Integer)
    comments = db.Column(db.Text)
    
    user = db.relationship("User")
    item = db.relationship("Item")

    
    
class Purchace(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    itemId = db.Column(db.Integer, db.ForeignKey('item.id'))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    user = db.relationship("User")
    item = db.relationship("Item")

    
db.create_all()
