from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from FreshCorner.model import db, User, Product, Category

# Define request parsers
product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str, required=True, help='Name is required')
product_parser.add_argument('MFD', type=str, required=True, help='MFD is required')
product_parser.add_argument('EXP', type=str, required=True, help='EXP is required')
product_parser.add_argument('rate', type=int, required=True, help='Rate is required')
product_parser.add_argument('description', type=str, required=True, help='Description is required')
product_parser.add_argument('image', type=str, required=True, help='Image is required')
product_parser.add_argument('mimetype', type=str, required=True, help='Mimetype is required')
product_parser.add_argument('quantity', type=int, required=True, help='Quantity is required')

category_parser = reqparse.RequestParser()
category_parser.add_argument('name', type=str, required=True, help='Name is required')

# Define response fields
product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'MFD': fields.String,
    'EXP': fields.String,
    'rate': fields.Integer,
    'description': fields.String,
    'image': fields.String,
    'mimetype': fields.String,
    'quantity': fields.Integer
}

category_fields = {
    'id': fields.Integer,
    'name': fields.String
}

# Define API resources
class ProductResource(Resource):
    @marshal_with(product_fields)
    def get(self, id):
        product = Product.query.get(id)
        if product:
            return product
        else:
            return {'message': 'Product not found'}, 404

    @marshal_with(product_fields)
    def put(self, id):
        args = product_parser.parse_args()
        product = Product.query.get(id)
        if product:
            product.name = args['name']
            product.MFD = args['MFD']
            product.EXP = args['EXP']
            product.rate = args['rate']
            product.description = args['description']
            product.image = args['image']
            product.mimetype = args['mimetype']
            product.quantity = args['quantity']
            db.session.commit()
            return product
        else:
            return {'message': 'Product not found'}, 404

    def delete(self, id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Product deleted'}
        else:
            return {'message': 'Product not found'}, 404

class ProductListResource(Resource):
    @marshal_with(product_fields)
    def get(self):
        products = Product.query.all()
        return products

    @marshal_with(product_fields)
    def post(self):
        args = product_parser.parse_args()
        product = Product(
            name=args['name'],
            MFD=args['MFD'],
            EXP=args['EXP'],
            rate=args['rate'],
            description=args['description'],
            image=args['image'],
            mimetype=args['mimetype'],
            quantity=args['quantity']
        )
        db.session.add(product)
        db.session.commit()
        return product, 201

class CategoryResource(Resource):
    @marshal_with(category_fields)
    def get(self, category_id):
        category = Category.query.get(category_id)
        if category:
            return category
        else:
            return {'message': 'Category not found'}, 404

    @marshal_with(category_fields)
    def put(self, category_id):
        args = category_parser.parse_args()
        category = Category.query.get(category_id)
        if category:
            category.name = args['name']
            db.session.commit()
            return category
        else:
            return {'message': 'Category not found'}, 404

    def delete(self, category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return {'message': 'Category deleted'}
        else:
            return {'message': 'Category not found'}, 404

class CategoryListResource(Resource):
    @marshal_with(category_fields)
    def get(self):
        categories = Category.query.all()
        return categories

    @marshal_with(category_fields)
    def post(self):
        args = category_parser.parse_args()
        category = Category(name=args['name'])
        db.session.add(category)
        db.session.commit()
        return category, 201

# Define API endpoints


