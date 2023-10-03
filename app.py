from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_mail import Mail, Message
import random
import string
import re
import time





app = Flask(__name__, template_folder='C:\\Users\\a0952\\Topic\\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:user1234@localhost/name'
app.config['SECRET_KEY'] = 'your_secret_key'


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
        except AssertionError as ae:
            print("validate error:", ae)
            flash(str(ae), 'danger')
            return render_template('login.html')
        except Exception as e:
            print("Error occurred:", e)
            db.session.rollback()
            flash('Registration faild. Please try again.', 'danger')
            return render_template('login.html')

    return render_template('login.html')



#忘記密碼
@app.route('/reset', methods=['GET','POST'])
def reset():
    Email = request.form.get('Email')
    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    msg = Message('Reset Your Password', sender=request.form.get('sender_email', 'default@example.com'), recipients=[Email])
    msg.body = f"Here's your password reset token: {token}"
    Mail.send(msg)
    
    flash('Password reset token has been sent to your email,','success')
    return redirect(url_for('forgot_password'))


#功能主頁面
@app.route('/home')
def home():
    return render_template('home.html')


'''
#倒數計時器
@app.route('/timestart', methods = ['GET','POST'])
def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='\r')  # \r更新倒數計時
        time.sleep(1)
        num_of_secs -= 1

    print('Countdown finished.    ')  # 額外的空格是為了覆蓋之前的倒計時，以確保它顯示正確


time_input = input('Input time in MM:SS format: ')

minutes, seconds = map(int, time_input.split(':'))# 使用 split() 方法根據 ":" 分割輸入的字串，得到分鐘和秒數

total_seconds = minutes*60+seconds  # 計算總秒數

countdown(total_seconds)'''

if __name__=="__main__":
    app.run(debug=True)