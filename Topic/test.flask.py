from flask import Flask ,jsonify
from flask_mysqldb import MySQL
import mysql.connector
import json

app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'user1234'
app.config['MYSQL_DB'] = 'sql_tutorial'
app.config['MYSQL_PORT'] = 3306


mysql = MySQL(app)

@app.route('/', methods=['GET'])
def CONNECT_DB():
    CS = mysql.connection.cursor()
    if CS:
        print("資料庫開啟成功")
    else:
        print("資料庫開啟失敗")


    CS.execute('''SELECT * FROM 8000english_words''')
    Executed_DATA = CS.fetchall()
    if Executed_DATA:
        print("抓取資料成功")
    else:
        print("抓取資料失敗")

    print(Executed_DATA)
    response = app.response_class(
    response=json.dumps(Executed_DATA, ensure_ascii=False),
    status=200,
    mimetype='application/json'
    )
    return response


if __name__=='__main__':
    app.run(debug=True)