import pytest
from app import schemas  
from jose import jwt, JWTError
from app.config import settings

    
def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Welcome to my app where I developed my first APIs with FastAPI!'
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email":"miguel@gmail.com", "password":"123456"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "miguel@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username":test_user['email'], "password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key , algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@gmail.com", "123456", 403),
    ("miguel@gmail.com", "000000", 403),
    ("wrongemail@gmail.com", "worngpassword", 403),
    (None, "123456", 422),
    ("miguel@gmail.com", None, 422)
    ])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={'username':email, 'password':password})
    assert res.status_code == status_code
    
