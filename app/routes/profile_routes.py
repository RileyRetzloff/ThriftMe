from flask import Blueprint, render_template, request, redirect, session, send_file
from ..models.pipeline import Users,db
profile = Blueprint('main', __name__)
import base64


#################
@profile.route('/profile', methods=['POST','GET'])
def render_profile():
    # Return user to signup if the user is not logged in, i.e., username returns None
    username = session.get('username')

    if username is None:
        print("No user is logged in.")
        return render_template('signup.html')

    user = Users.get_by_username(username)

    if user is None:
        print(f"User {username} not found.")
        return render_template('signup.html')

    profile_picture_base64 = None

    if user.profile_picture is not None:
        profile_picture_base64 = base64.b64encode(user.profile_picture).decode('utf-8')

    print(f"User {username} is logged in.")
    return render_template('profile.html', username=username, profile_picture=profile_picture_base64)
    
##################

@profile.route('/edit_profile', methods=['POST','GET'])
def render_profile_settings():
    username = session.get('username')
    user = Users.get_by_username(username)
    profile_picture_base64 = None
    if user.profile_picture is not None:
        profile_picture_base64 = base64.b64encode(user.profile_picture).decode('utf-8')

    return render_template('profile_settings.html', username = username, profile_picture=profile_picture_base64)

##################

@profile.route('/edit_username', methods=['POST','GET'])
def render_edit_profile_user():
    username = session.get('username')
    user = Users.get_by_username(username)

    if request.method == 'POST':
                
        newUsername = request.form.get('newUsername')
        
        if newUsername and user is not None:
            user.username = newUsername
            db.session.commit()
            session['username'] = newUsername
        return redirect('/edit_profile')  

    return render_template('index.html', username=username)  

##################

@profile.route('/edit_profile_pic', methods=['POST', 'GET'])
def render_edit_profile():
    username = session.get('username')
    user = Users.get_by_username(username)
    allowed_extensions = {'jpg', 'jpeg'}
    profile_picture_base64 = None  # Default value

    if request.method == 'POST' and 'image' in request.files:
        new_pfp = request.files['image']
        if '.' in new_pfp.filename and new_pfp.filename.rsplit('.', 1)[1].lower() in allowed_extensions:
            # Update the user's profile picture in the database
            user.profile_picture = new_pfp.read()
            db.session.commit()

            profile_picture_base64 = base64.b64encode(user.profile_picture).decode('utf-8')

        else:
            return render_template('profile_settings.html', username=username, profile_picture=profile_picture_base64)

    return render_template('profile_settings.html', username=username, profile_picture=profile_picture_base64)

##################

@profile.route('/logout', methods=['POST','GET'])
def logout():
    session.clear()
    return render_template('index.html')