import os
import requests
from flask import Blueprint, url_for, render_template, request, redirect, flash
from werkzeug.utils import secure_filename


admin = Blueprint('admin', __name__, url_prefix='/admin')

baseURL = "http://127.0.0.1:5000"


#===================================================PRODUCT METHODS====================================


@admin.route('/addproduct', methods=['GET', 'POST'])

def add_product():
    cat = requests.get(f"{baseURL}/categories").json()
    if request.method == 'POST':
        # Get the form data from the request
        poster = request.files ['image']

        filename = secure_filename(poster.filename)
        poster.save("static/product_img/"+filename)
        mimetype = poster.mimetype
        data = {
            'name': request.form['name'],
            'MFD': request.form['MFD'],
            'EXP': request.form['EXP'],
            'rate': int(request.form['rate']),
            'description': request.form['description'],
            'image': filename,
            'mimetype': mimetype,
            'quantity': int(request.form['quantity']),
            'category_id': int(request.form['category_id'])
        }
        response = requests.post(f"{baseURL}/products", json=data)
        if response.status_code == 201:
            return redirect(url_for('admin'))
        else:
            return "Error adding product."

    # If it's a GET request, simply render the addproduct form
    return render_template('admin/addproduct.html', categories = cat)

@admin.route('/update_product/<int:id>', methods = ['PUT','GET'])

def update_product(id):
    prod = requests.get(f"{baseURL}/products/{id}")
    if prod.status_code == 200:
        if  request.method == 'POST':
            poster = request.files ['image']

            filename = secure_filename(poster.filename)
            poster.save("static/product_img/"+filename)
            mimetype = poster.mimetype

            data = {
                'name': request.form['name'],
                'MFD': request.form['MFD'],
                'EXP': request.form['EXP'],
                'rate': int(request.form['rate']),
                'description': request.form['description'],
                'image': filename,
                'mimetype': mimetype,
                'quantity': int(request.form['quantity']),
                'category_id': int(request.form['category_id'])
            }
            response = requests.put(f"{baseURL}/products/{id}", json=data)
            if response.status_code == 201:
                return redirect(url_for('admin'))
            else:
                return "Error updating product."

        return render_template('admin/update_product.html')

@admin.route('/delete_product/<int:id>', methods = ['GET', 'POST'])

def delete_product(id):
    prod = requests.get(f"{baseURL}/products/{id}")
    if prod.status_code == 200:
        response = requests.delete(f'{baseURL}/products/{id}')
        product_data = prod.json()
        image_filename = product_data.get('image', '')
        if image_filename:
            image_path = os.path.join("static/product_img", image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)
            else:
                flash("Associated image not found.", 'warning')
        if response.status_code == 200:
            flash("Product Deleted Succesfully.")
            return redirect(url_for('admin'))
        else:
            return 'error in deleting product'
    return "can't find product you wanna delete."
        

@admin.route('/add_category', methods=['GET','POST'])

def add_category():
    if request.method == 'POST':
        data = {
            'name': request.form["name"]
        }
        res = requests.post(f"{baseURL}/categories", json=data)
        if res.status_code == 201:
            flash("Category Added Successfully!")
            return redirect(url_for('admin'))
        else:
            return 'error in creating category '
    return render_template('admin/add_category.html')
        
@admin.route('/delete_category/<int:id>', methods=['GET', 'POST'])

def delete_category(id):
    catg = requests.get(f"{baseURL}/categories/{id}")
    if catg.status_code == 200:
        res = requests.delete(f"{baseURL}/categories/{id}")
        if res.status_code == 200:
            flash('Category deleted successfuly')
            return redirect(url_for('admin'))
        else:
            flash('There are products associted with this category. Please delete them first.')
            return redirect(url_for('admin'))
    else:
        return "can't find the product you wanna delete"


@admin.route('/update_category/<int:id>', methods=['GET', 'POST'])

def update_category(id):
    catg = requests.get(f"{baseURL}/categories/{id}")
    if catg.status_code == 200:
        c = catg.json()
        if request.method == 'POST':
            data = {
                'name':request.form['name']
            }
            requests.put(f"{baseURL}/categories/{id}", json=data)
            return redirect(url_for('admin'))
        return render_template('admin/update_category.html', c = c)

        