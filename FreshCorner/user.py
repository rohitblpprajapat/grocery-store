from flask import render_template, Blueprint
from flask_login import login_required, current_user
from FreshCorner.model import PurchaseHistory
from flask import current_app as app

@app.route('/dashboard')
@login_required
def user_dashboard():
    user = current_user
    purchase_history = PurchaseHistory.query.filter_by(user_id=user.id).all()
    
    return render_template('dashboard.html', user=user, purchase_history=purchase_history)


