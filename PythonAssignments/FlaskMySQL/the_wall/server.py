from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'd41d8cd98f00b204e9800998ecf8427e'
mysql = MySQLConnector(app,'mydb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/the_wall')
def the_wall():
    return render_template('the_wall.html')

@app.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    email_query = "SELECT email from users where email= :email"
    email_data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    email_check = mysql.query_db(email_query, email_data)

    user_login_query = "SELECT id, email, password , first_name from users where email= :email"
    login_data = {'email' :email}
    

    user_data_check = mysql.query_db(user_login_query, login_data)[0]
    print user_data_check
    session['user'] = user_data_check['id']
    session['first_name'] = user_data_check['first_name']
    return redirect('/the_wall')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register/process', methods=["POST"])
def register_process():
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    print query
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'password': request.form['password']
           }
    session['user'] = data['first_name']
    mysql.query_db(query, data)
    return redirect('/the_wall')

@app.route('/log_off')
def log_off():
    session.clear()
    return redirect('/')

app.run(debug=True)