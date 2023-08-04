import os
from flask import Flask
from FreshCorner.model import db
from flask_restful import Api
def create_app():
    app = Flask(__name__, template_folder="templates")

    app.config['SECRET_KEY'] = 'FJSLDJFLSJFSJDFKJSDLFKJSD'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'database', 'store.db')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    db.init_app(app)
    app.app_context().push()
    api = Api(app)
    print(app.jinja_loader.list_templates())

    return app, api

app, api = create_app()

from FreshCorner.authentication import *
from apis.api import *

api.add_resource(ProductResource, '/products/<int:id>')
api.add_resource(ProductListResource, '/products')
api.add_resource(CategoryResource, '/categories/<int:category_id>')
api.add_resource(CategoryListResource, '/categories')

if __name__ == '__main__':
    app.run(debug=True)
