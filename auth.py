from flask import Flask, request, render_template
import pickle

auth = Flask(__name__)


@auth.route('/')
def hello_world():
    return render_template("login.html")
database={'nachi':'123','james':'aac','karthik':'asdsf'}

@auth.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
      return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
           return render_template('home.html',name=name1)


if __name__ == '__main__':
  try:
    auth.rundebug=True, host='0.0.0.0',port='8080', ssl_context=('/home/aldasvmuser/cert.pem', '/home/aldasvmuser/privkey.pem')
  except:
    print('unable to open port')


