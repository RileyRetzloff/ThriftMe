from flask import Flask,render_template, request,redirect,abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

