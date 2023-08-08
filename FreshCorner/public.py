from flask import render_template,request
import requests
from flask import current_app as app
from FreshCorner.model import *
from sqlalchemy import or_


@app.route('/', methods = ['GET'])
def home():
    catg = requests.get('http://127.0.0.1:5000/categories').json()
    prods = requests.get('http://127.0.0.1:5000/products').json()
    return render_template("index.html", products = prods, categories = catg)

@app.route('/categories', methods = ['GET'])
def categories():
    cats = requests.get(url='http://127.0.0.1:5000/categories').json()
    return render_template('categories.html', categories = cats)

@app.route('/product/<int:product_id>')
def detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)





@app.route('/search/products', methods=['GET'])
def search_products():
    search_term = request.args.get('search_term')


    
    products = Product.query.filter(
        or_(Product.name.ilike(f'%{search_term}%'), Product.rate.ilike(f'%{search_term}'), Product.MFD.ilike(f'%{search_term}'))
    ).all()
    categories = Category.query.filter(
        (Category.name.ilike(f'%{search_term}'))
    ).all()

    return render_template('search_results.html', search_term=search_term, products=products, categories = categories)
