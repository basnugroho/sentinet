from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Havingfun123@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lrpwlvahyxcfvi:717bf058cb3571889734de02acc9cfa36c066daf65c2d9ba5b0e1cfa321a07a0@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d8e95e9db6p1hi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

@app.route('/')
def index():
    return render_template('index.html', quote = "kindness needs no translation") 

@app.route('/about')
def about():
    return '<h1>Hello World from about page.</h1>'

@app.route('/quotes')
def quotes():
    return '<h1>Life is a journey.</h1>'

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    return redirect(url_for('index.html'))

