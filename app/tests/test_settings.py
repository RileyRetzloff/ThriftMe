
import random
import string
from app.models.pipeline import Users




def test_adding_and_deleting_user(client):
    dummy_username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    dummy_email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '@' +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    dummy_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


    #send data to the create account endpoint
    client.post("/create", data = {'username': dummy_username, 'email': dummy_email, 'password': dummy_password})
    response = client.get('/settings')

    assert Users.query.count() == 1
    assert Users.query.first().username == dummy_username
    assert response.status_code == 200
   
    response = client.get('/delete')


    assert Users.query.count() == 0
    assert Users.query.first() == None
   