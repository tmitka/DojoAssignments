from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'W9Zzyj$3h#4$ck6kEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_submit():
    if len(request.form['name']) < 1:
        flash('Name cannot be empty')
    else:
        flash('Success')
    if len(request.form['comment']) < 1:
        flash('please enter a comment')
    elif len(request.form['comment']) > 120:
        flash('comment cannot be longer than 120 characters')
    return redirect('/')

app.run(debug=True)