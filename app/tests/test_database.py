
import os
from app.database import db,bcrypt
from sqlalchemy import inspect,text
import random
import string 
from app.models.pipeline import Users

def test_connection(client):

    inspector = inspect(db.engine)
    all_tables = inspector.get_table_names()
    
    ##testing if it is switching to the test database when testing
    assert db.engine.url.render_as_string(hide_password=False) == f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("TEST_DB_NAME")}'
    for table_name in all_tables:
        res = db.session.execute(text(f" select count(*) from {table_name};"))
        count = res.scalar()
        assert count == 0
    

#idk how to check the password
def test_adding_user(client):
    dummy_username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    dummy_email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '@' +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    dummy_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


    #send data to the create account endpoint
    response = client.post("/create", data = {'username': dummy_username, 'email': dummy_email, 'password': dummy_password})

    print(response)
    assert Users.query.count() == 1
    assert Users.query.first().username == dummy_username
    assert Users.query.first().email == dummy_email
    assert response.status_code == 302
