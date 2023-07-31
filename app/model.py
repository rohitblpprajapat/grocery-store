from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)
    
    @property
    def is_active(self):
        return True
    def get_id(self):
        return str(self.id)
    
class Product(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    MFD = db.Column(db.String())
    EXP = db.Column(db.String())
    rate = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String())
    image = db.Column(db.Text, unique = True, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable = False)
    catagory = db.relationship('Category', backref=db.backref('products', lazy=True))
    
class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable=False)
    
