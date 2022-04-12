from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_Access_token


# we can use the below code to test the database or just add _test to the end of the original one
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {"email":"miguel@gmail.com", "password":"123456"}
    res = client.post("/users/", json={"email":"miguel@gmail.com", "password":"123456"})
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_Access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}
    return client
    
    
@pytest.fixture
def test_posts(test_user, session):
    post_data = {"title":"Test post", "body":"Test body"}
    res = client.post("/posts/", json=post_data)
    assert res.status_code == 201
    new_post = res.json()
    new_post['user_id'] = test_user['id']
    return new_post