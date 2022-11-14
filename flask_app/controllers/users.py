from flask_app import app
from flask import render_template, redirect, request, session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def allUsers():
    return render_template('allUsers.html', allUsers=User.getAllUsers())

@app.route('/users/new')
def newUser():
    return render_template('newUsers.html')

@app.route('/users/create', methods=['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
        }
    User.createUser(data)
    return redirect ('/users/new')

