import random
import string

from app.models.pipeline import Users,CommunityPost,CommunityPostComment,Album,Photo
from app.database import db
from io import BytesIO
from flask import url_for,app


def test_route(client):

    #create a user and log them in to get a session going
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '@' +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    client.post("/create", data = {'username': username, 'email': email, 'password': password})

    response = client.get('/community')
    
    assert response.data is not None
    assert b"<h2>Community</h2>" in response.data



    """
    This test simulates file uploads using the create post endpoint. 
    Be careful running it over and over as it will fill app/static/user_images with a bunch 
    of copies of the same pictures since there is no code that deletes pictures from the filesystem.
    """
    
def test_create_post(client,app):
    #create a user and log them in to get a session going
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '@' +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    client.post("/create", data = {'username': username, 'email': email, 'password': password})


    with open('app/tests/file_test/Y2KBaggyJean.png', 'rb') as file:  
        
        client.post('/create_post', data = {'post-title' : 'test_post', 
                                                       'upload-pictures' :(BytesIO(file.read()),'Y2KBaggyJean.png')})
    

    post = CommunityPost.query.first()
    photo = Photo.query.first()
    with app.test_request_context():
        response = client.post(url_for('community.community_post_', community_post_id = post.get_id()))


    print(response.data)
    assert post.post_content.encode() in response.data
    assert photo.photo_url.encode() in response.data
    


