from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import login_required, current_user
from FreshCorner.model import *

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user = current_user
    product = Product.query.get_or_404(product_id)
    
    # Check if the product is already in the user's cart
    if Cart.query.filter_by(user_id=user.id, product_id=product.id).first():
        flash('Product is already in your cart.', 'warning')
        return redirect(url_for('detail', product_id=product.id))
    
    new_cart_item = Cart(user=user, product=product)
    db.session.add(new_cart_item)
    db.session.commit()
    
    flash('Product added to your cart.', 'success')
    return redirect(url_for('detail', product_id=product.id))


@cart_bp.route('/view_cart')
@login_required
def view_cart():
    user = current_user
    cart_items = Cart.query.filter_by(user_id=user.id).all()
    
    return render_template('cart.html', cart_items=cart_items)

@cart_bp.route('/update_cart/<int:cart_id>', methods=['POST'])
@login_required
def update_cart(cart_id):
    new_quantity = int(request.form.get('new_quantity'))
    cart_item = Cart.query.get_or_404(cart_id)
    
    if new_quantity <= 0:
        flash('Quantity must be greater than 0.', 'warning')
    else:
        cart_item.quantity = new_quantity
        db.session.commit()
        flash('Cart item quantity updated.', 'success')
    
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    db.session.delete(cart_item)
    db.session.commit()
    
    flash('Product removed from your cart.', 'success')
    return redirect(url_for('cart.view_cart'))


def checkout(user, cart_items):
    try:
        for cart_item in cart_items:
            product = cart_item.product
            if cart_item.quantity <= product.quantity:
                purchase = PurchaseHistory(user=user, product=product, quantity=cart_item.quantity)
                db.session.add(purchase)
                
                product.quantity -= cart_item.quantity
                db.session.add(product)
                
                db.session.delete(cart_item) 
                
            else:
                flash(f"{product.name} is out of stock. Only {product.quantity} available.")
        
        db.session.commit()
        flash("Purchase successful!", "success")
        return redirect(url_for("cart.view_cart")) 
        
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while processing your purchase.", "danger")
        return redirect(url_for("cart.view_cart"))  


@cart_bp.route("/checkout")
@login_required
def checkout_route():
    user = current_user 
    cart_items = user.cart  

    checkout(user, cart_items)
    return redirect(url_for("user_dashboard"))

