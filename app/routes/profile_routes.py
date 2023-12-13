from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..models.pipeline import Users,db
from ..utils import upload_file

profile = Blueprint('main', __name__)


#################
@profile.route('/profile', methods=['POST','GET'])
def render_profile():
    username = session.get('username')
    if username == None:
        print("No user is logged in.")
        return render_template('signup.html')
    else:
        print(f"User {username} is logged in.")
        return render_template('profile.html', username=username)
    
##################

@profile.route('/edit_profile', methods=['POST','GET'])
def render_profile_settings():
    username = session.get('username')
    return render_template('profile_settings.html', username = username)

##################

@profile.route('/edit_username', methods=['POST','GET'])
def render_edit_profile_user():
    username = session.get('username')
    user = Users.get_by_username(username)
    newUsername = request.form.get('newUsername')
    user.username = newUsername
    db.session.commit()

    return redirect('/edit_profile')    

##################

@profile.route('/edit_profile_pic', methods=['POST','GET'])
def render_edit_profile_profile():
    username = session.get('username')

    return render_template('profile_settings.html', username = username)

@profile.route('/logout', methods=['POST','GET'])
def logout():
    session.clear()
    return render_template('index.html')