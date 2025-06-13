import json

def test_login_success(test_client):
    response = test_client.post('/auth/login', json={
        "username": "Jedidah",
        "password": "Jeddy@1"
    })
    data = response.get_json()
    
    assert response.status_code == 200
    assert "access_token" in data


def test_login_failure(test_client):
    response = test_client.post('/auth/login', json={
        "username": "invalid_user",
        "password": "wrong_password"
    })
    data = response.get_json()

    assert response.status_code == 401
    assert "access_token" not in data
    assert "error" in data or "msg" in data
