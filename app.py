from flask import Flask, url_for, redirect
from model import *
from flask_login import LoginManager, login_required, logout_user, UserMixin




#============================================================ C O N F I G U R T I O N =================================================================


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = 'FJSLDJFLSJFSJDFKJSDLFKJSD'
db.init_app(app)

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
    return "this will be login page"
    

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
    
    
