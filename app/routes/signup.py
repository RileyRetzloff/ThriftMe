from flask import Blueprint, abort, render_template, request, redirect, url_for
from ..database import db
from app.models.pipeline import Users
signup = Blueprint('signup', __name__)

@signup.route('/signup')
def display():
    return render_template('signup.html')


@signup.route('/')
def home():
    return render_template('profile.html')

@signup.post('/create')
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    if not username or not password or not email:
        abort(400)
    new_user = Users(username = username, email = email,password = password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')