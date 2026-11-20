from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about/<user>')
def about(user):
    return f'<h1> About page my of my {user} luv</h1>'
