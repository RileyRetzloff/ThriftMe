from flask import Blueprint, render_template, request, redirect, url_for
from ..database import db
from pipeline import users
signup = Blueprint('signup', __name__)

@signup.route('/')
def display():
    return render_template('signup.html')


@signup.post('/signup')
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    new_user = users(username = username, email = email,password = password)
    db.session.add(new_user)
    db.session.commit()