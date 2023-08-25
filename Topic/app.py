from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='C:\\Users\\a0952\\Topic\\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:user1234@localhost/name'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(20), unique=True, nullable=False)
    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        Email = request.form.get('Email')
        Username = request.form.get('Username')
        Password = request.form.get('password')

        print("Received Data:")
        print("Email:", Email)
        print("Username:", Username)
        print("Password:", Password)

        # TODO: Check if email already exists

        new_user = User(Email=Email,Username=Username, Password=Password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            print("Error occurred:", e)
            db.session.rollback()
            return "Registraction failed", 500

    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)