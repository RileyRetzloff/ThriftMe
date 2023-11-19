from flask import Blueprint, render_template, request, redirect, url_for

# Create Blueprint
index = Blueprint('index', __name__)

# Define main index route
@index.route('/')
def home():
    return render_template('index.html')

""""
TODO 
Make route files with blueprints for all of the functions below.
The reason the app is running is because they are all registerd under the index blueprint.
"""

#COMMUNITY PAGE
@index.route('/community')
def community():
    return render_template('community.html')

#CONTACT PAGE
@index.route('/contact')
def contact():
    return render_template('contact.html')

#MARKETPLACE PAGE
@index.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

#USER PAGE
@index.route('/user')
def user():
    return render_template('user.html')