from flask import Flask, redirect, render_template, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'a5g6HKI03!$^dsii$$@@siofhs'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if len(request.form['first_name']) < 1:
        flash('First name cannot be empty')

    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty")

    if len(request.form['email']) < 1:
        flash('Email must be submitted')

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address")

    if len(request.form['password']) < 1:
        flash('Password required')

    if len(request.form['password']) < 9:
        flash('Password must be more than 8 characters')

    if request.form['password'] != request.form['password_confirm']:
        flash("Passwords do not match")
    
    if request.form['first_name'].isdigit():
        print 'is digit'
        flash('Name cannot have a number')

    else:
        flash("Thank's for submitting your information")
    return redirect('/')    

app.run(debug=True)