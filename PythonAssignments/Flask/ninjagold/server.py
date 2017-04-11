from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime

app =Flask(__name__)
app.secret_key = 'gold'

@app.route('/')
def index():

    if 'gold' not in session.keys():
        session['gold'] = 0
    if 'history' not in session.keys():
        session['history'] = []


    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process_money():
    choice = request.form['building']
    print 'you picked', choice

    gold_earned = 0

    if choice == 'farm':
        gold_earned = random.randint(10, 20)
    elif choice == 'cave':
        gold_earned = random.randint(5, 10)
    elif choice == 'house':
        gold_earned = random.randint(2,5)
    elif choice == 'casino':
        gold_earned = random.randint(-50, 50)

    session['gold'] += gold_earned
    session['history'].append("Earned {} gold from the {} ({})".format(gold_earned, choice, datetime.now()))
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold')
    session.pop('history')
    return redirect('/')

app.run(debug=True)
