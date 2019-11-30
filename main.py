import pymysql,json
from app import app
from db_config import mysql
from flask import flash, session, render_template, request, redirect


@app.route('/login')
def login():

        return render_template('login.html')

@app.route('/load', methods=['GET'])
def load():
                #Load DB
                conn = mysql.connect()
                cursor = conn.cursor()
                sql ="""SELECT prodname FROM product_master"""
                cursor.execute(sql)
                print ("Connected to database..")
                rows=cursor.fetchall()
                records=[]
                if rows is None:
                                conn.close()
                                flash ("No Records..");
                                return redirect('/login')
                else:
                        return json.dumps(rows)  

@app.route('/search', methods=['GET','POST'])
def search():
                param=request.args.get('prodname')
                print (" in Search api...",param)
                #Load DB by value
                conn = mysql.connect()
                cursor = conn.cursor()
                sql ="""SELECT * FROM product_master where prodname=%s"""
                print ("url... ", request.url)
                print ("param...",param)
                cursor.execute(sql,param)
                print ("Connected to database..")
                rows=cursor.fetchall()
                if rows is None:
                                conn.close()
                                flash ("No Records..");
                                return redirect('/login')
                else:
                        return json.dumps(rows)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

