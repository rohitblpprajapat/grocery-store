from flask import Flask, url_for, redirect, render_template, request, session, flash
from model import *
from flask_login import LoginManager, login_required, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




#============================================================ C O N F I G U R T I O N =================================================================


app = Flask(__name__)
app.config['SECRET_KEY'] = 'FJSLDJFLSJFSJDFKJSDLFKJSD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'

db.init_app(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


#============================================================ R O U T E S =================================================================
@app.route('/', methods=['GET'])
def home():
    return "this will be home page"
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(username = username).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid Credentials')
            return redirect(url_for('login'))
        else:
            session['user_id'] = user.id
            session['logged_in_user'] = True
            flash("Login successful Username: %s" % user.username)
            return redirect(url_for('home'))
        
            
    return render_template('login_user.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        
        user = User(name=name, username=username, password=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Successfully registered')
        return redirect(url_for('login'))
    
    return render_template('register.html')

        

    

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
    
    
