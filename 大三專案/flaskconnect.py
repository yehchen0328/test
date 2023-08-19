from flask import Flask, request, redirect, url_for, render_template
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__, template_folder='C:/Users/a0952/Templates')
mysql = MySQL(app)

@app.route('/login', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')


    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="user1234",
        database="name"
    )

    cursor = db.cursor()
    sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
    val = (email, password)
    cursor.execute(sql, val)

    db.commit()

    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

