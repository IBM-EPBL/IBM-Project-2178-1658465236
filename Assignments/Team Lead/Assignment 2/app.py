from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         NAME = request.form['NAME']
         EMAILID = request.form['EMAIL']
         MOBILENUMBER = request.form['MOBILE']
         CITY = request.form['CITY']
         STATE =request.form['STATE']
         COUNTRY =request.form['COUNTRY']
         PASSWORD = request.form['PASSWORD']
         
         with sql.connect("Users.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users (NAME,EMAIL,MOBILE,CITY,STATE,COUNTRY,PASSWORD) VALUES (?,?,?,?,?,?,?)",(NAME,EMAILID,MOBILENUMBER,CITY,STATE,COUNTRY,PASSWORD))
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("list.html",msg = msg)
         con.close()


@app.route('/list')
def list():
   con = sql.connect("Users.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Users")
   
   students = cur.fetchall();
   return render_template("list.html", students = students)


if __name__ == '__main__':
   app.run(debug = True)
