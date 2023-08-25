from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='C:\\Users\\a0952\\Topic\\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:user1234@localhost/name'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(200), unique=True, nullable=False)
    Username = db.Column(db.String(200), nullable=False)
    Password = db.Column(db.String(200), nullable=False)


#登入畫面
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')

        #TODO: 驗證名稱與密碼是否正確
        user = User.query.filter_by(Username=Username, Password=Password).first()

        if user:
            # 如果用戶存在，重定向到主頁
            print('User found')
            return redirect(url_for('home'))
        else:
            print("User not found")
            # 如果用戶不存在，返回一條訊息通知用戶
            return "Invalid Username or password", 401

    return render_template('signin.html')


#註冊畫面
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

        new_user = User(Email=Email,Username=Username, Password=Password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            print("Error occurred:", e)
            db.session.rollback()
            return "Registraction failed", 500

    return render_template('login.html')


#功能主頁面
@app.route('/home')
def home():
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)