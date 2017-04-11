from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'W9Zzyj$3h#4$ck6kEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    validation_failed = False

    if len(session['name']) < 1:
        flash('Name cannot be empty')
        validation_failed = True
    if len(session['comment']) < 1:
        flash('please enter a comment')
        validation_failed = True    
    if len(session['comment']) > 120:
        flash('comment cannot be longer than 120 characters')
        validation_failed = True

    if validation_failed == True:        
        return redirect('/')
    else:
        return render_template('info.html')

app.run(debug=True)