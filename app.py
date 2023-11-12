from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__, root_path='content/')

#HOME PAGE
@app.route('/')
def index():
    return render_template('index.html')

#COMMUNITY PAGE
@app.route('/community')
def community():
    return render_template('community.html')

#CONTACT PAGE
@app.route('/contact')
def contact():
    return render_template('contact.html')

#CREATE LISTING PAGE
@app.route('/create_listing')
def create_listing():
    return render_template('create_listing.html')

#LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')

#MARKETPLACE PAGE
@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

#PROFILE PAGE
@app.route('/profile')
def profile():
    return render_template('profile.html')

#SETTINGS PAGE
@app.route('/settings')
def settings():
    return render_template('settings.html')

#USER PAGE
@app.route('/user')
def user():
    return render_template('user.html')
