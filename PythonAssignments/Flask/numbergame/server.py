from flask import Flask, render_template, redirect, request, session
import random
app =Flask(__name__)
app.secret_key = 'mitka'


@app.route('/')
def index():
    winningnumber = random.randrange(0, 101)
    if 'winningnumber' in session:
        print session['winningnumber']
    else:
        session['winningnumber'] = winningnumber
        print session['winningnumber']

    return render_template('index.html')
 

app.run(debug=True)