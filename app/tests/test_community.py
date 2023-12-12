import random
import string

from app.models.pipeline import Users,CommunityPost,CommunityPostComment,Album
from app.database import db


def test_route(client):

    #create a user and log them in to get a session going
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '@' +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    client.post("/create", data = {'username': username, 'email': email, 'password': password})

    response = client.get('/community')
    
    print(response.data)
    assert response.data is not None
    assert b"<h2>Community</h2>" in response.data




    


