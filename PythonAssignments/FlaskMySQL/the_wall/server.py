from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'd41d8cd98f00b204e9800998ecf8427e'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/the_wall', methods=["POST"])
def the_wall():
    return render_template('the_wall.html')

@app.route('/register')
def register():
    return render_template('register.html')

app.run(debug=True)