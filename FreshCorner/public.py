from flask import Blueprint, render_template, url_for, jsonify
import requests
from flask import current_app as app


@app.route('/', methods = ['GET'])
def home():
    catg = requests.get('http://127.0.0.1:5000/categories').json()
    prods = requests.get('http://127.0.0.1:5000/products').json()
    return render_template("index.html", products = prods, categories = catg)

@app.route('/categories', methods = ['GET'])
def categories():
    cats = requests.get(url='http://127.0.0.1:5000/categories').json()
    return render_template('categories.html', categories = cats)

@app.route('/products', methods = ['GET'])
def products():
    prods = requests.get('http://127.0.0.1:5000/products')
    return render_template('products.html', products = prods)
