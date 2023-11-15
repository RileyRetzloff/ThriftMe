from flask import Flask,render_template, request,redirect,abort,url_for

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/profile', methods=['POST','GET'])
# def profile():
#     return render_template('profile.html')
@app.get('/')
def display():
    return render_template('login.html')


@app.get('/login')
def sign_up():
    # if the email matches the password given
    email = request.form.get('email')
    # redirect to the user page
    # else, throw an error or refresh the page to try again
    print(f'Hello {email}')
    return render_template('login.html')