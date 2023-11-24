from ..database import db

#TODO make classes for the other tables

"""
User class that makes people able to login to the app
Also serves as a central hub to all other tables
This establishes user activities such as liking posts, commenting ect.
"""
class Users(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.LargeBinary)
    public_access = db.Column(db.Boolean, nullable=False)


    albums = db.relationship('Album', back_populates='user')

"""
Album stores refrences to photos 
[One User] -> [Many albums(posts)]
[One album] -> [Many photos]
"""
    
class Album(db.Model):
    __tablename__ = 'albums'

    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    album_name = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', back_populates = 'albums')
    photos = db.relationship('Photo' , back_populates='album')


"""
Table to store many photos 
"""
class Photo(db.Model):
    __tablename__ = 'photos'

    photo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.album_id', ondelete='CASCADE'), nullable=False)
    photo_data = db.Column(db.LargeBinary)

    album = db.relationship('Album', back_populates='photos')