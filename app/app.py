from flask import Flask,render_template, request,redirect,abort,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['POST','GET'])
def profile():
    return render_template('profile.html')