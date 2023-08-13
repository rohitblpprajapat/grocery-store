from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)
    purchase_history = db.relationship('PurchaseHistory', backref='user', lazy=True)
    cart = db.relationship('Cart', backref='user', lazy=True)
    
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
    unit = db.Column(db.String())
    description = db.Column(db.String())
    image = db.Column(db.Text, unique = False, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable = False)
    catagory = db.relationship('Category', backref=db.backref('products', lazy=True))
    deleted = db.Column(db.Boolean(), default=False)
    
    
class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable=False)
    deleted = db.Column(db.Boolean(), default=False)
    
    
class PurchaseHistory(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    purchase_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('purchase_history', lazy=True))
    quantity = db.Column(db.Integer, nullable=True)



class Cart(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('carts', lazy=True))
    quantity = db.Column(db.Integer(), nullable=True)

    
