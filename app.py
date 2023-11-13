from flask import Flask,render_template, request,redirect,abort,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['POST','GET'])
def profile():
    return render_template('profile.html')



@app.post('/login')
def sign_up(email,password):
    # if the email matches the password given
    # redirect to the user page
    # else, throw an error or refresh the page to try again
    return redirect('profile/<')