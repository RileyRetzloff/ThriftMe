from flask import Blueprint, render_template, request, redirect, url_for
login = Blueprint('login', __name__)

@login.route('/login')
def display():
    return render_template('login.html')

