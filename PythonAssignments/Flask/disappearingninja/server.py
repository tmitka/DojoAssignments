from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    return render_template('ninja_color.html', color=color)

app.run(debug=True)