from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_blogs():
    response = client.get('/blog/all')
    assert response.status_code == 200


def test_auth_error():
    response = client.post('/token', 
    data={'username': 'nonexistent', 
          'password': 'wrongpassword'})
    assert response.status_code == 404