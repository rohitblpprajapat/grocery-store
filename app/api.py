from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort
from flask import Flask, request
import werkzeug
from model import *

app = Flask(__name__)
api = Api(app)


prod_parser = reqparse.RequestParser()
prod_parser.add_argument(
    'name', fields.String
)







def abort_if(id):
    product = db.session.query(Product).filter(Product.id == id).first()
    if product is None:
        abort(404, message="Todo {} doesn't exists.".format(id))
        
        
class Product(Resource):
    def get(self, id):
        abort_if(id)
        return (db.session.query(Product).filter(Product.id == id).first())
        
    def put(self, id):
        product = db.session.query(Product).filter(Product.id == id).first()
        
    
    

# api.add_resource("Product", '/<int: di>')



api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)