from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    
    @property
    def is_active(self):
        return True
    def get_id(self):
        return str(self.id)
    
class Product(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(), nullable=False)
    MFD = db.Column(db.String())
    EXP = db.Column(db.String())
    rate = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String())
    image = db.Column(db.Text, unique = True, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    
class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable=False)
    
