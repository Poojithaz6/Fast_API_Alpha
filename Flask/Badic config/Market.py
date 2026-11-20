from flask import Flask
app=Flask(__name__)
@app.route('/')
def greet():
    return '<h1>Hello world</h1>'

@app.route('/about/<user>')
def about(user):
    return f'<h1> About page my of my {user} luv</h1>'