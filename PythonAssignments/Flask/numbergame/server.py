from flask import Flask, render_template, redirect, request, session
import random
app =Flask(__name__)
app.secret_key = 'mitka'


@app.route('/')
def index():
    if 'winningnumber' not in session.keys():
        session['winningnumber'] = random.randrange(0, 101)
        
    if 'guess' in session.keys():
        print "Your guess is", session['guess']
        if session['guess'] > session['winningnumber']:
            print "Your guess: {} > the winning number:{}".format(session['guess'], session['winningnumber'])
            session['answer'] = "Too high"
    
        elif session['guess'] < session['winningnumber']:
            print "Your guess: {} < the winning number {}".format(session['guess'], session['winningnumber'])
            session['answer'] = "Too low"
        else: 
            print "session guress: {} is right".format(session['guess'])
            session['answer'] = "You got it" 

    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    print 'Guess is'
    session['guess'] = int(request.form['guess'])
    print session['guess']
    return redirect('/')
 

app.run(debug=True)