from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required
import pickle
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
mysql = MySQL()
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
app.config['MYSQL_USER'] = 'web'
app.config['MYSQL_PASSWORD'] = 'webPass'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = 'localhost' 
mysql.init_app(app)


# Default - Show Data
@app.route("/") 
def hello(): 
    return render_template("login.html")
    database = {'admin':'admin'}

    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    Results=[]
    for row in rv: #Format the Output Results and add to return string
      Result={}
      Result['Name']=row[0]
      Result['Email']=row[1]
      Result['ID']=row[2]
      Result['DOB']=row[3]
      Result['Course']=row[4]
      Result['Phone']=row[5]
      Result['Address']=row[6]
      Results.append(Result)
    response={'Results':Results, 'count':len(Results)}
    ret=app.response_class(
      response=json.dumps(response),
      status=200,
      mimetype='application/json'
    )
    return ret #Return the data in a string format


if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('/home/aldasvmuser/cert.pem', '/home/aldasvmuser/privkey.pem')) #Run the flask app at port 8080





# Login authentication function
@app.route('/login',methods=['POST','GET'])
def login():
    loginname=request.form['username']
    loginpassword=request.form['password']
    if loginname not in database:
      return render_template('login.html',info='Invalid User')
    else:
        if database[loginname]!=loginpassword:
            return render_template('login.html',info='Invalid Password')
        else:
           return render_template('main.html',name=loginname)



# Add Student function - gets input from user and executes an SQL command
# to add student to the database
@app.route("/add") 
def add():
  name = request.args.get('name')
  email = request.args.get('email')
  dob = request.args.get('dob')
  course = request.args.get('course')
  phone = request.args.get('phone')
  address = request.args.get('address')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s='''INSERT INTO students(studentName, email, dob, course, phone, address) VALUES('{}','{}','{}','{}','{}','{}');'''.format(name,email,dob,course,phone,address)
  cur.execute(s)
  mysql.connection.commit()

  return '{"Result":"Success"}'


# Delete Student function - gets input from user and executes an SQL command
# to delete the relevant entries from the database
@app.route("/delete")
def delete():
 id = request.args.get('id')
 cur = mysql.connection.cursor() #create a connection to the SQL instance
 s='''DELETE s.* FROM students s WHERE studentID='{}';'''.format(id)
 cur.execute(s)
 mysql.connection.commit()
 return '{"Result":"Success"}'


# Update Student function - gets input from user and executes an SQL command
# to update relevant information fields of a student 
@app.route("/update")
def update():
  id = request.args.get('id')
  name = request.args.get('name')
  email = request.args.get('email')
  dob = request.args.get('dob')
  course = request.args.get('course')
  phone = request.args.get('phone')
  address = request.args.get('address')
  cur = mysql.connection.cursor() #create a connection to the SQL instance
  s='''UPDATE students s SET studentName='{}', email='{}', dob='{}', course='{}', phone='{}', address='{}' WHERE studentID='{}';'''.format(name,email,dob,course,phone,address,id)
  cur.execute(s)
  mysql.connection.commit()
  return '{"Result":"Success"}'

#