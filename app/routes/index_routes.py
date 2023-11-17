from flask import Blueprint, render_template, request, redirect, url_for

# Create Blueprint
index = Blueprint('index', __name__)

# Define main index route
@index.route('/')
def home():
    return render_template('index.html')

#COMMUNITY PAGE
@index.route('/community')
def community():
    return render_template('community.html')

#CONTACT PAGE
@index.route('/contact')
def contact():
    return render_template('contact.html')

#CREATE LISTING PAGE
@index.route('/create_listing')
def create_listing():
    return render_template('create_listing.html')

#LOGIN PAGE
@index.route('/login')
def login():
   return render_template('login.html')

#MARKETPLACE PAGE
@index.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

#PROFILE PAGE
@index.route('/profile')
def profile():
    return render_template('profile.html')

#SETTINGS PAGE
@index.route('/settings')
def settings():
    return render_template('settings.html')

#USER PAGE
@index.route('/user')
def user():
    return render_template('user.html')