# Login authentication function
@app.route("/login",methods=['POST', 'GET'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
      session['logged_in'] = True
      return render_template('main.html')

    else:
      flash('wrong password!')
      print("Password incorrect")
      return render_template('login.html', info="Invalid username and password combination")
      # return index() 

#     database = {'admin':'admin'}
#     return render_template("index.html")

#     loginname=request.form['username']
#     loginpassword=request.form['password']
#     if loginname not in database:
#       return render_template('index.html',info='Invalid User')
#     else:
#         if database[loginname]!=loginpassword:
#             return render_template('index.html',info='Invalid Password')
#         else:
#            return render_template('main.html',name=loginname)



